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
        question="""# Aplatissement de liste

Implémentez une fonction :

```python
def flatten(xs):
```

qui aplatit récursivement une liste de listes (potentiellement imbriquées de façon arbitraire)
en une liste plate à une seule dimension, en préservant l'ordre des éléments.

Règles précises :
- Les éléments non-listes sont conservés tels quels dans l'ordre.
- Les listes vides imbriquées ne produisent aucun élément.
- Si `xs` n'est pas une liste (par exemple un entier ou une chaîne), la fonction doit lever une
  exception de type `TypeError`.

## Exemples

```python
flatten([])                      # []
flatten([1, 2, 3])               # [1, 2, 3]
flatten([1, [2, [3, [4]], 5]])   # [1, 2, 3, 4, 5]
flatten([[1, 2], [], [3]])       # [1, 2, 3]
```
""").reponse
)