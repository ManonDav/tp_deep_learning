import evaluator


task = evaluator.get_task_description("12_word_frequencies")
code = """import re
from collections import defaultdict

def word_frequencies(text: str) -> dict:
    if not text:
        return {}

    # Use regex to find all words, considering apostrophes as part of the word
    # The regex matches sequences of letters and apostrophes, ensuring that apostrophes are part of the word
    words = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)*", text)

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Count the frequency of each word
    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1

    # Convert defaultdict to a regular dict before returning
    return dict(frequency)"""
implementation= evaluator.test_implementation("12_word_frequencies", code)
print(implementation)
