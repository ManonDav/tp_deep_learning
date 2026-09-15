# Élément le plus fréquent

Implémentez une fonction :

```python
def most_frequent(xs):
```

qui renvoie l'élément le plus fréquent d'une liste non vide.

Règles précises :
- En cas d'égalité (plusieurs éléments ayant la même fréquence maximale), renvoyer celui qui
  apparaît **en premier** dans la liste.
- La liste est garantie non vide (vous n'avez pas à gérer le cas vide).
- Les éléments peuvent être de tout type hachable (entiers, chaînes).

## Exemples

```python
most_frequent([1, 3, 1, 2, 3, 1])   # 1
most_frequent([3, 1, 3, 1])          # 3  (3 et 1 ex æquo, 3 apparaît en premier)
most_frequent(["a", "b", "a"])       # "a"
most_frequent([7])                    # 7
```
