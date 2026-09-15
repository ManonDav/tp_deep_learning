# Regroupement d'anagrammes

Implémentez une fonction :

```python
def group_anagrams(words) -> list:
```

qui reçoit une liste de chaînes et renvoie une liste de groupes : chacun contient les mots qui
sont des anagrammes les uns des autres (mêmes lettres, même nombre d'occurrences, casse
insensible).

Règles précises :
- Deux mots sont des anagrammes s'ils ont exactement les mêmes lettres avec les mêmes
  fréquences, en ignorant la casse (`"Tea"` et `"eat"` sont des anagrammes).
- La comparaison doit ignorer la casse, mais les mots du groupe sont renvoyés **tels quels**
  (casse d'origine préservée).
- L'ordre des groupes et l'ordre des mots dans chaque groupe ont la liberté : les résultats ne
  sont vérifiés que comme ensembles de groupes.
- Les chaînes non vides n'ont que des caractères alphabétiques.

## Exemples

```python
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# ex. [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
group_anagrams([])                       # []
group_anagrams(["abc"])                  # [["abc"]]
group_anagrams(["Tea", "ate", "EAT"])    # ex. [["Tea", "ate", "EAT"]]
```

## Dernière implémentation

```python
from collections import defaultdict

def group_anagrams(words) -> list:
    anagram_groups = defaultdict(list)

    for word in words:
        # Convertir le mot en minuscule pour normaliser la comparaison
        key = word.lower()
        anagram_groups[key].append(word)

    # Convertir les valeurs en liste de listes
    return list(anagram_groups.values())
```

Cette implémentation n'a pas passé tous les tests.
Voici les tests échoués:
```python
result = normalize(group_anagrams(["Tea", "ate", "EAT"]))
expected = normalize([["Tea", "ate", "EAT"]])
assert result == expected

result = normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
expected = normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
assert result == expected
``` 
Ton implémentation ne regroupe pas correctement les anagrammes.
Le problème vient de la manière dont tu construis la clé du dictionnaire :

```python
key = word.lower()
```

Cette clé permet seulement de regrouper les mots qui sont identiques sans tenir compte de la casse. Elle ne permet pas de reconnaître deux mots qui contiennent les mêmes lettres dans un ordre différent.

Par exemple :

```python
"eat".lower()  # "eat"
"tea".lower()  # "tea"
"ate".lower()  # "ate"
```

Ces trois mots obtiennent donc trois clés différentes alors qu'ils sont tous des anagrammes.

Il faut construire une clé qui représente les lettres du mot indépendamment de leur ordre, tout en ignorant la casse.

Par exemple, après avoir converti le mot en minuscules, tu peux trier ses lettres :

```python
"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"
```

Les trois mots auront alors la même clé et pourront être placés dans le même groupe.

Attention : il faut conserver le mot original dans le groupe. La conversion en minuscules sert uniquement à construire la clé de comparaison. Par exemple :

```python
["Tea", "ate", "EAT"]
```

doit rester :

```python
[["Tea", "ate", "EAT"]]
```

et non devenir :

```python
[["tea", "ate", "eat"]]
```

La logique attendue est donc :

1. Parcourir chaque mot de `words`.
2. Créer une clé permettant d'identifier les anagrammes, en ignorant la casse et l'ordre des lettres.
3. Vérifier si cette clé existe déjà dans les groupes.
4. Si elle existe, ajouter le mot original au groupe correspondant.
5. Sinon, créer un nouveau groupe avec ce mot.
6. À la fin, retourner la liste des groupes.

Par exemple :

```python
["eat", "tea", "tan", "ate", "nat", "bat"]
```

doit produire des groupes équivalents à :

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

L'ordre des groupes et l'ordre des mots dans les groupes n'a pas d'importance.

Corrige donc l'implémentation en utilisant une clé basée sur les lettres du mot plutôt que sur le mot lui-même.