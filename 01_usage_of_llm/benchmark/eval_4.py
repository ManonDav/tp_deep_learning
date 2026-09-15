import evaluator


task = evaluator.get_task_description("04_most_frequent")
code = """def most_frequent(xs):
    frequency = {}
    max_freq = 0
    most_freq_element = None

    for element in xs:
        frequency[element] = frequency.get(element, 0) + 1

        if frequency[element] > max_freq:
            max_freq = frequency[element]
            most_freq_element = element
        elif frequency[element] == max_freq and most_freq_element is None:
            most_freq_element = element

    return most_freq_element"""
implementation= evaluator.test_implementation("04_most_frequent", code)
print(implementation)
