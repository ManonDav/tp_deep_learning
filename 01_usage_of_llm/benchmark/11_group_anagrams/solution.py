from collections import defaultdict

def group_anagrams(words) -> list:
    anagram_groups = defaultdict(list)

    for word in words:
        # Convertir le mot en minuscule pour normaliser la comparaison
        key = word.lower()
        anagram_groups[key].append(word)

    # Convertir les valeurs en liste de listes
    return list(anagram_groups.values())