# Préfixe commun le plus long

Implémentez une fonction :

```python
def longest_common_prefix(strs) -> str:
```

qui reçoit une liste de chaînes et renvoie le plus long préfixe commun à toutes les chaînes,
ou la chaîne vide `""` s'il n'existe aucun préfixe commun.

Règles précises :
- Le préfixe doit être commun à **toutes** les chaînes de la liste.
- Si une chaîne est vide, ou si les premières lettres diffèrent dès la première position, le
  préfixe commun est `""`.
- La comparaison est sensible à la casse.

## Exemples

```python
longest_common_prefix(["flower", "flow", "flight"])   # "fl"
longest_common_prefix(["dog", "racecar", "car"])      # ""
longest_common_prefix(["interspecies", "interstellar", "interstate"])  # "inters"
longest_common_prefix(["", "b"])                      # ""
longest_common_prefix(["single"])                     # "single"
```
