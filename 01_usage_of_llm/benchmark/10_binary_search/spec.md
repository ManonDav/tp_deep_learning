# Recherche dichotomique

Implémentez une fonction :

```python
def binary_search(xs, target) -> int:
```

qui renvoie l'indice de `target` dans la liste triée `xs`, ou `-1` si `target` n'y figure pas.

Règles précises :
- `xs` est une liste **triée en ordre croissant** d'entiers (vous pouvez la supposer triée).
- La fonction doit utiliser l'algorithme de **recherche dichotomique** en `O(log n)` :
  elle doit diviser l'espace de recherche en deux à chaque itération en comparant `target` à
  l'élément médian. Un parcours linéaire (`target in xs`, `xs.index`, boucle simple) n'est pas
  acceptable.
- S'il y a plusieurs occurrences, renvoyer n'importe quelle position valide.
- Une liste vide renvoie `-1`.

## Exemples

```python
binary_search([-5, 0, 3, 7, 9, 11], 7)   # 3
binary_search([1, 2, 3, 4, 5], 1)        # 0
binary_search([1, 2, 3, 4, 5], 5)        # 4
binary_search([1, 2, 3, 4, 5], 0)        # -1
binary_search([], 3)                     # -1
```
