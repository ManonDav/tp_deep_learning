import evaluator


task = evaluator.get_task_description("15_two_sum")
implementation= evaluator.test_implementation("15_two_sum", """def two_sum(nums, target) -> list:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []""")
print(implementation)
