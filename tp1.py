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
        question="""# Fibonacci efficace

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
""").reponse
)