import evaluator


task = evaluator.get_task_description("11_group_anagrams")
code = """from collections import defaultdict

def group_anagrams(words) -> list:
    anagram_groups = defaultdict(list)

    for word in words:
        # Convertir le mot en minuscule pour normaliser la comparaison
        key = word.lower()
        anagram_groups[key].append(word)

    # Convertir les valeurs en liste de listes
    return list(anagram_groups.values())"""
implementation= evaluator.test_implementation("11_group_anagrams", code)
print(implementation)
