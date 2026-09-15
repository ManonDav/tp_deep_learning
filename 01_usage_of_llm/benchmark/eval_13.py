import evaluator


task = evaluator.get_task_description("13_fibonacci")
code = """def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b"""
implementation= evaluator.test_implementation("13_fibonacci",code )
print(implementation)
