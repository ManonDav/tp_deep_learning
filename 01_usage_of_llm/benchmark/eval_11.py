import evaluator


task = evaluator.get_task_description("11_group_anagrams")
implementation= evaluator.test_implementation("11_group_anagrams", """def group_anagrams(words) -> list:
    if not words:
        return []
    
    anagram_groups = {}
    
    for word in words:
        # Convertir le mot en minuscule pour normaliser la comparaison
        key = word.lower()
        # Si le groupe n'existe pas, le créer
        if key not in anagram_groups:
            anagram_groups[key] = []
        # Ajouter le mot tel quel au groupe
        anagram_groups[key].append(word)

    # Retourner la liste des groupes
    return list(anagram_groups.values())""")
print(implementation)
