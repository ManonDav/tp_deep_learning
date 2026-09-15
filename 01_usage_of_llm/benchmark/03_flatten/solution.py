def flatten(xs):
    if not isinstance(xs, list):
        raise TypeError("Input must be a list")

    result = []
    for item in xs:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result