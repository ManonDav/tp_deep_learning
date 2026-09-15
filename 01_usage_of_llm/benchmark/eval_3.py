import evaluator


task = evaluator.get_task_description("03_flatten")
code = """def flatten(xs):
    if not isinstance(xs, list):
        raise TypeError("Input must be a list")

    result = []
    for item in xs:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result"""
implementation= evaluator.test_implementation("03_flatten", code)
print(implementation)
