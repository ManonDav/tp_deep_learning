import evaluator


task = evaluator.get_task_description("02_run_length_encode")
implementation= evaluator.test_implementation("02_run_length_encode", """def run_length_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return ''.join(result)""")
print(implementation)
