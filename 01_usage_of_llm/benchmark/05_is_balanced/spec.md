# Parenthèses équilibrées

Implémentez une fonction :

```python
def is_balanced(s: str) -> bool:
```

qui détermine si les parenthèses, crochets et accolades de `s` sont correctement imbriqués et
équilibrés. Seuls ces trois types de délimiteurs comptent : les autres caractères sont ignorés.

Règles précises :
- Chaque ouverture `(`, `[`, `{` doit être fermée par son délimiteur correspondant `)`, `]`, `}`.
- La fermeture doit respecter l'ordre d'imbrication (une fermeture doit correspondre à
  l'ouverture la plus récente non fermée).
- Une chaîne sans délimiteur (ou vide) est considérée comme équilibrée (`True`).

## Exemples

```python
is_balanced("()")                # True
is_balanced("()[]{}")            # True
is_balanced("({[]})")            # True
is_balanced("(]")                # False
is_balanced("([)]")              # False
is_balanced("((())")            # False  (3 ouvertures, 2 fermetures)
is_balanced("")                  # True
is_balanced("abc")               # True  (aucun délimiteur)
```
