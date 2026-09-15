"""Helpers to drive the code-generation benchmark.

Provides functions used by the student harness:

- ``get_task_description(task_id)`` returns the *spec.md* text of a task, i.e. the
  prompt to send to the LLM.
- ``test_implementation(task_id, code)`` writes ``code`` to the task's ``solution.py`` and runs
  the task's unit tests, returning ``(valid, message)`` where ``message`` is a useful error
  report when the implementation is invalid, or an empty string on success.
- ``score_implementations(implementations)`` runs a batch of implementations and returns the
  ``(score, failed)`` pair: the success rate and the list of failed task identifiers.

A task is identified either by its folder name (``"07_merge_intervals"``) or by its
zero-indexed / one-indexed number (``6`` or ``7``).
"""

from __future__ import annotations

import importlib.util
import io
import os
import signal
import sys
import traceback
from pathlib import Path

BENCHMARK_DIR = Path(__file__).resolve().parent

# Wall-clock budget for a single test function. Guards against implementations that are
# correct-looking but pathologically slow (e.g. exponential recursive fibonacci), which
# would otherwise hang the whole batch instead of failing with a useful report.
TEST_TIMEOUT_SECONDS = 5


class _TestTimeout(Exception):
    pass


def _run_with_timeout(fn, seconds: float) -> None:
    """Run ``fn()``, raising ``_TestTimeout`` if it doesn't return within ``seconds``.

    Uses ``SIGALRM`` and therefore only works in the main thread on Unix; if unavailable
    (e.g. on Windows, or off the main thread), falls back to running without a timeout.
    """
    if not hasattr(signal, "SIGALRM"):
        fn()
        return

    def _on_alarm(signum, frame):
        raise _TestTimeout(f"test exceeded {seconds}s (likely an inefficient implementation)")

    previous_handler = signal.signal(signal.SIGALRM, _on_alarm)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        fn()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)


def _resolve_task(task_id: str | int) -> Path:
    if isinstance(task_id, int) or (isinstance(task_id, str) and task_id.isdigit()):
        n = int(task_id)
        if n <= 0:
            raise ValueError(f"task number must be >= 1, got {n}")
        matches = sorted(
            BENCHMARK_DIR.glob(f"{n:02d}_*")
        )
        if not matches:
            raise ValueError(f"no task numbered {n} in {BENCHMARK_DIR}")
        task_dir = matches[0]
    else:
        task_dir = BENCHMARK_DIR / str(task_id)
        if not task_dir.is_dir():
            raise ValueError(f"no task directory named {task_id!r} in {BENCHMARK_DIR}")
    spec = task_dir / "spec.md"
    tests = task_dir / "test_task.py"
    if not spec.is_file() or not tests.is_file():
        raise FileNotFoundError(f"task {task_dir.name} missing spec.md or test_task.py")
    return task_dir


def get_task_description(task_id: str | int) -> str:
    """Return the *spec.md* text of the given task (the prompt to send to the LLM)."""
    task_dir = _resolve_task(task_id)
    return (task_dir / "spec.md").read_text(encoding="utf-8")


def _run_tests(task_dir: Path) -> tuple[bool, list[str]]:
    """Run the task's ``test_task.py`` unit tests in-process.

    Returns ``(all_passed, failures)`` where ``failures`` is a list of human-readable
    strings describing each failed test (test name + traceback).
    """
    test_path = task_dir / "test_task.py"
    test_module_name = f"task_{task_dir.name}_tests"

    # Evict any previously imported solution/test module so each task loads its own fresh copy.
    for cached in list(sys.modules):
        if cached == "solution" or cached == test_module_name or cached.startswith("task_"):
            del sys.modules[cached]

    sys.path.insert(0, str(task_dir))
    try:
        try:
            spec = importlib.util.spec_from_file_location(test_module_name, test_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception as exc:  # import error, often a broken solution
            tb = traceback.format_exc(limit=4).strip()
            return False, [f"Error while loading tests for {task_dir.name}:\n{tb}"]

        failures = []
        for name in dir(module):
            if not name.startswith("test_"):
                continue
            test = getattr(module, name)
            if not callable(test):
                continue
            try:
                _run_with_timeout(test, TEST_TIMEOUT_SECONDS)
            except _TestTimeout as exc:
                failures.append(f"{name}: {exc}")
            except Exception as exc:
                report_lines = io.StringIO()
                traceback.print_exc(file=report_lines)
                failures.append(
                    f"{name}: {type(exc).__name__}: {exc}\n{report_lines.getvalue().strip()}"
                )

        return not failures, failures
    finally:
        # test_task.py inserts its own directory into sys.path too (so it can be run
        # standalone), so more than one copy of task_dir may be present here: drop them all.
        sys.path[:] = [p for p in sys.path if p != str(task_dir)]


def test_implementation(task_id: str | int, code: str) -> tuple[bool, str]:
    """Test ``code`` against the given task's unit tests.

    Writes ``code`` to the task's ``solution.py`` (overwriting any previous file), then runs
    the task's ``test_task.py`` functions.

    Returns a ``(valid, message)`` tuple:

    - ``valid`` is ``True`` if every test passed (message is ``""``);
    - otherwise ``valid`` is ``False`` and ``message`` holds a concise report (which tests
      failed and the traceback) suitable to feed back to an LLM.
    """
    task_dir = _resolve_task(task_id)
    solution = task_dir / "solution.py"
    solution.write_text(code, encoding="utf-8")

    ok, failures = _run_tests(task_dir)
    if ok:
        return True, ""

    message = (
        f"Implementation for {task_dir.name} is invalid. "
        f"{len(failures)} test(s) failed:\n" + "\n\n".join(failures)
    )
    return False, message


def score_implementations(implementations: dict[str | int, str]) -> tuple[float, list[str]]:
    """Test a batch of implementations and return ``(score, failed)``.

    ``implementations`` maps a task identifier (folder name or number, as accepted by
    ``test_implementation``) to the implementation code to test.

    Returns:

    - ``score``: the success rate (number of tasks passing all their tests divided by the total
      number of tasks provided), a float in ``[0.0, 1.0]``. An empty mapping yields ``0.0``.
    - ``failed``: the sorted list of identifiers of the tasks whose implementation was invalid.
    """
    if not implementations:
        return 0.0, []

    failed = []
    for task_id, code in implementations.items():
        valid, _ = test_implementation(task_id, code)
        if not valid:
            failed.append(task_id)

    names = sorted(str(t) for t in failed)
    score = (len(implementations) - len(failed)) / len(implementations)
    return score, names