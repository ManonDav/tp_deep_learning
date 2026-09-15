import dspy

# Ollama tourne directement sur ton PC
OLLAMA_BASE = "http://localhost:11434"
MODEL = "qwen3:8b"


# Configuration de DSPy pour utiliser Ollama en local
lm = dspy.LM(
    f"ollama/{MODEL}",
    api_base=OLLAMA_BASE,
    think=False,
    cache=False,
)

dspy.configure(lm=lm)


class ReponseSignature(dspy.Signature):
    """Répond à une question de programmation par du code Python."""

    question: str = dspy.InputField()
    reponse: str = dspy.OutputField()


repondre = dspy.Predict(ReponseSignature)


print(
    repondre(
        question="""# Recherche dichotomique

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
""").reponse
)