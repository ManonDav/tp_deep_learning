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
        question="""# Entier → romain

Implémentez une fonction :

```python
def int_to_roman(n: int) -> str:
```

qui convertit un entier strictement positif en chaîne de chiffres romains.

Règles précises :
- `n` est un entier tel que `1 <= n < 4000`.
- On utilise la convention soustractive standard : `4` s'écrit `IV`, `9` s'écrit `IX`,
  `40` s'écrit `XL`, `90` s'écrit `XC`, `400` s'écrit `CD`, `900` s'écrit `CM`.
- Les symboles sont uniquement des majuscules.

Symboles disponibles : `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`.

## Exemples

```python
int_to_roman(3)      # "III"
int_to_roman(4)      # "IV"
int_to_roman(9)      # "IX"
int_to_roman(58)     # "LVIII"
int_to_roman(1994)   # "MCMXCIV"
int_to_roman(1)      # "I"
```
""").reponse
)