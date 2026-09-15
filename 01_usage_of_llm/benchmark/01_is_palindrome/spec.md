# Palindrome

Implémentez une fonction :

```python
def is_palindrome(s: str) -> bool:
```

qui détermine si `s` est un palindrome en ignorant la casse, les espaces et la ponctuation :
seuls les caractères alphanumériques comptent pour la comparaison.

Cas particuliers :
- Une chaîne vide, ou une chaîne ne contenant aucun caractère alphanumérique, est considérée comme un palindrome (`True`).

## Exemples

```python
is_palindrome("Was it a car or a cat I saw?")  # True
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("Hello")  # False
is_palindrome("")  # True
is_palindrome("   ")  # True
is_palindrome("12321")  # True
is_palindrome("12345")  # False
```
