# Fibonacci efficace

Implémentez une fonction :

```python
def fibonacci(n: int) -> int:
```

qui renvoie le `n`-ième nombre de Fibonacci, avec `F(0) = 0` et `F(1) = 1`.

Règles précises :
- `n` est un entier positif ou nul (`0 <= n`).
- La fonction doit être **efficace** : elle doit traiter `n = 100` quasi instantanément.
  Une implémentation naïvement récursive (appels redondants, complexité exponentielle) n'est
  pas acceptable. Utilisez une itération, la programmation dynamique, ou la récursion avec
  mémoïsation.
- `F(0) = 0`, `F(1) = 1`, `F(2) = 1`, `F(10) = 55`.

## Exemples

```python
fibonacci(0)    # 0
fibonacci(1)    # 1
fibonacci(2)    # 1
fibonacci(10)   # 55
fibonacci(100)  # 354224848179261915075
```
