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
        question="""# Romain → entier

Implémentez une fonction :

```python
def roman_to_int(s: str) -> int:
```

qui convertit un nombre écrit en chiffres romains en entier.

Règles précises :
- L'entrée est une chaîne non vide composée uniquement de caractères romains valides
  (`I, V, X, L, C, D, M`, en majuscules).
- On utilise la convention soustractive standard : `IV` vaut 4, `IX` vaut 9, `XL` vaut 40,
  `XC` vaut 90, `CD` vaut 400, `CM` vaut 900.
- Un symbole placé avant un symbole de valeur supérieure se soustrait ; sinon il s'additionne.

Valeurs de base : `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`.

## Exemples

```python
roman_to_int("III")    # 3
roman_to_int("IV")     # 4
roman_to_int("IX")     # 9
roman_to_int("LVIII")  # 58
roman_to_int("MCMXCIV")  # 1994
```
""").reponse
)