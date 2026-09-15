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
        question="""# Fusion d'intervalles

Implémentez une fonction :

```python
def merge_intervals(intervals):
```

qui reçoit une liste d'intervalles, chacun représenté par une paire `[début, fin]` d'entiers
(bornes incluses), et renvoie une nouvelle liste avec tous les intervalles qui se chevauchent
ou sont adjacents fusionnés.

Règles précises :
- Deux intervalles `[a, b]` et `[c, d]` avec `c <= b` se chevauchent ou sont adjacents et sont
  fusionnés en `[min(a, c), max(b, d)]`.
- Les intervalles en entrée ne sont pas nécessairement triés.
- La liste résultante doit être **triée** par début croissant.
- Chaque intervalle en entrée vérifie toujours `début <= fin`.
- Une liste vide donne une liste vide.

## Exemples

```python
merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])   # [[1, 6], [8, 10], [15, 18]]
merge_intervals([[1, 4], [4, 5]])                      # [[1, 5]]   (adjacents)
merge_intervals([[6, 8], [1, 2], [3, 5]])              # [[1, 2], [3, 5], [6, 8]]
merge_intervals([])                                    # []
```
""").reponse
)