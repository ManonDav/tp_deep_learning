import evaluator


task = evaluator.get_task_description("10_binary_search")
implementation= evaluator.test_implementation("10_binary_search", """def binary_search(xs, target) -> int:
    left = 0
    right = len(xs) - 1

    while left <= right:
        mid = (left + right) // 2
        if xs[mid] == target:
            return mid
        elif xs[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1""")
print(implementation)
