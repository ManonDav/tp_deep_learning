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
        question="""# Compression par plages (RLE)

Implémentez une fonction :

```python
def run_length_encode(s: str) -> str:
```

qui encode `s` par compression de plages (*run-length encoding*) : chaque suite de caractères
identiques consécutifs est remplacée par le nombre d'occurrences suivi du caractère.

Règles précises :
- Le compte est **toujours** inclus, même s'il vaut 1 (donc `"abc"` devient `"1a1b1c"`, pas `"abc"`).
- La comparaison est sensible à la casse : `'a'` et `'A'` sont des caractères différents.
- Une chaîne vide donne une chaîne vide.

## Exemples

```python
run_length_encode("aaabbbccd")  # "3a3b2c1d"
run_length_encode("abcd")  # "1a1b1c1d"
run_length_encode("")  # ""
run_length_encode("aAaa")  # "1a1A2a"
```
""").reponse
)