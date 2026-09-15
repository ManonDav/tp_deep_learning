import evaluator


task = evaluator.get_task_description("01_is_palindrome")
implementation= evaluator.test_implementation("01_is_palindrome", """import re

def is_palindrome(s: str) -> bool:
    processed = re.sub(r'[^a-z0-9]', '', s.lower())
    return processed == processed[::-1]""")
print(implementation)
