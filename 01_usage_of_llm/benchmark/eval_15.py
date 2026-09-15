import evaluator


task = evaluator.get_task_description("15_two_sum")
code = """def two_sum(nums, target) -> list:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []"""
implementation= evaluator.test_implementation("15_two_sum", code )
print(implementation)
