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
        question="""# Fréquence des mots

Implémentez une fonction :

```python
def word_frequencies(text: str) -> dict:
```

qui renvoie un dictionnaire associant à chaque mot la fréquence de son apparition dans `text`.

Règles précises :
- Les mots sont délimités par tout caractère non alphabétique (espaces, ponctuation, chiffres).
- La comparaison ignore la casse : `"The"` et `"the"` comptent pour le même mot, qui est stocké
  en **minuscules** dans le dictionnaire.
- Un mot peut contenir des apostrophes internes (ex. `"l'eau"`) : l'apostrophe fait partie du
  mot.
- Les mots n'apparaissant pas dans le texte ne figurent pas dans le dictionnaire.
- Une chaîne vide (ou sans mot) donne un dictionnaire vide.

## Exemples

```python
word_frequencies("The cat and the dog.")  # {"the": 2, "cat": 1, "and": 1, "dog": 1}
word_frequencies("a-b c! a.")             # {"a": 2, "b": 1, "c": 1}
word_frequencies("")                      # {}
word_frequencies("l'eau est l'eau")       # {"l'eau": 2, "est": 1}
```
""").reponse
)