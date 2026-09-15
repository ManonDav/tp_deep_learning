import re
from collections import defaultdict

def word_frequencies(text: str) -> dict:
    if not text:
        return {}

    # Utilisation de regex pour trouver tous les mots, en ignorant la casse
    words = re.findall(r"[\w']+", text.lower())

    # Comptage des fréquences
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1

    # Conversion en dict standard
    return dict(freq)