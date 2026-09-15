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
