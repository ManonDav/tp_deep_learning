# Deux nombres dont la somme est cible

Implémentez une fonction :

```python
def two_sum(nums, target) -> list:
```

qui reçoit une liste d'entiers `nums` et un entier `target`, et renvoie les **indices** des deux
éléments distincts dont la somme est égale à `target`.

Règles précises :
- On garantit qu'il existe **exactement une** paire de valeurs distinctes dont la somme vaut
  `target`. Vous n'avez pas à gérer l'absence de solution.
- L'ordre des deux indices renvoyés importe peu, mais les deux indices doivent être **distincts**
  et renvoyés dans une liste.
- Les deux éléments peuvent avoir la même valeur (ex. `[3, 3]` avec `target = 6`), mais il s'agit
  alors de deux positions différentes.
- Une implémentation en `O(n²)` (double boucle) fonctionne, mais une implémentation en `O(n)`
  à l'aide d'un dictionnaire est préférée.

## Exemples

```python
two_sum([2, 7, 11, 15], 9)   # [0, 1]
two_sum([3, 2, 4], 6)        # [1, 2]
two_sum([3, 3], 6)           # [0, 1]
two_sum([1, 2, 3], 5)        # [1, 2]
```
