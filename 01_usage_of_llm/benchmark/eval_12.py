import evaluator


task = evaluator.get_task_description("12_word_frequencies")
implementation= evaluator.test_implementation("12_word_frequencies", """import re
from collections import defaultdict

def word_frequencies(text: str) -> dict:
    if not text:
        return {}

    # Utilisation de regex pour trouver tous les mots, en ignorant la casse
    words = re.findall(r"\b[\w']+\b", text.lower())

    # Comptage des fréquences
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1

    # Conversion en dict standard
    return dict(freq)""")
print(implementation)
