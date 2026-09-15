# Fréquence des mots

Implémentez une fonction :

```python
def word_frequencies(text: str) -> dict:
```

qui renvoie un dictionnaire associant à chaque mot la fréquence de son apparition dans `text`.

Règles précises :
- Les mots sont délimités par tout caractère non alphabétique (espaces, ponctuation, chiffres).
- La comparaison ignore la casse : `"The"` et `"the"` comptent pour le même mot, qui est stocké
  en **minuscules** dans le dictionnaire.
- Un mot peut contenir des apostrophes internes (ex. `"l'eau"`) : l'apostrophe fait partie du
  mot.
- Les mots n'apparaissant pas dans le texte ne figurent pas dans le dictionnaire.
- Une chaîne vide (ou sans mot) donne un dictionnaire vide.

## Exemples

```python
word_frequencies("The cat and the dog.")  # {"the": 2, "cat": 1, "and": 1, "dog": 1}
word_frequencies("a-b c! a.")             # {"a": 2, "b": 1, "c": 1}
word_frequencies("")                      # {}
word_frequencies("l'eau est l'eau")       # {"l'eau": 2, "est": 1}
```

## Dernière implémentation

```python
import re
from collections import defaultdict

def word_frequencies(text: str) -> dict:
    if not text:
        return {}

    # Use regex to find all words, considering apostrophes as part of the word
    words = re.findall(r"[a-zA-Z]+('[a-zA-Z]+)*", text)

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Count the frequency of each word
    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1

    # Convert defaultdict to a regular dict before returning
    return dict(frequency)
```

Cette implémentation n'a pas passé tous les tests.
Voici les tests échoués:
```python
assert word_frequencies("hello hello hello") == {"hello": 3}
assert word_frequencies("a-b c! a.") == {"a": 2, "b": 1, "c": 1}
assert word_frequencies("The cat and the dog.") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
assert word_frequencies("l\'eau est l\'eau") == {"l\'eau": 2, "est": 1}
```
Il faut modifier ton code pour passer ces tests.
Prend en compte les caractères spéciaux.