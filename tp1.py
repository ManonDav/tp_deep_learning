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
        question="""# Élément le plus fréquent

Implémentez une fonction :

```python
def most_frequent(xs):
```

qui renvoie l'élément le plus fréquent d'une liste non vide.

Règles précises :
- En cas d'égalité (plusieurs éléments ayant la même fréquence maximale), renvoyer celui qui
  apparaît **en premier** dans la liste.
- La liste est garantie non vide (vous n'avez pas à gérer le cas vide).
- Les éléments peuvent être de tout type hachable (entiers, chaînes).

## Exemples

```python
most_frequent([1, 3, 1, 2, 3, 1])   # 1
most_frequent([3, 1, 3, 1])          # 3  (3 et 1 ex æquo, 3 apparaît en premier)
most_frequent(["a", "b", "a"])       # "a"
most_frequent([7])                    # 7
```

""").reponse
)