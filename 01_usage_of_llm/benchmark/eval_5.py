import evaluator


task = evaluator.get_task_description("05_is_balanced")
code = """def is_balanced(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack"""
implementation= evaluator.test_implementation("05_is_balanced", code)
print(implementation)
