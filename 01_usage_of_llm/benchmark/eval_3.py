import evaluator


task = evaluator.get_task_description("03_flatten")
implementation= evaluator.test_implementation("03_flatten", """def flatten(xs):
    if not isinstance(xs, list):
        raise TypeError("Input must be a list")

    result = []
    for item in xs:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result""")
print(implementation)
