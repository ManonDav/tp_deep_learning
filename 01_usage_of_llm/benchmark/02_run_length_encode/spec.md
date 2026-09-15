# Compression par plages (RLE)

Implémentez une fonction :

```python
def run_length_encode(s: str) -> str:
```

qui encode `s` par compression de plages (*run-length encoding*) : chaque suite de caractères
identiques consécutifs est remplacée par le nombre d'occurrences suivi du caractère.

Règles précises :
- Le compte est **toujours** inclus, même s'il vaut 1 (donc `"abc"` devient `"1a1b1c"`, pas `"abc"`).
- La comparaison est sensible à la casse : `'a'` et `'A'` sont des caractères différents.
- Une chaîne vide donne une chaîne vide.

## Exemples

```python
run_length_encode("aaabbbccd")  # "3a3b2c1d"
run_length_encode("abcd")  # "1a1b1c1d"
run_length_encode("")  # ""
run_length_encode("aAaa")  # "1a1A2a"
```
