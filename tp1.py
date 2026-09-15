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
        question="""# Parenthèses équilibrées

Implémentez une fonction :

```python
def is_balanced(s: str) -> bool:
```

qui détermine si les parenthèses, crochets et accolades de `s` sont correctement imbriqués et
équilibrés. Seuls ces trois types de délimiteurs comptent : les autres caractères sont ignorés.

Règles précises :
- Chaque ouverture `(`, `[`, `{` doit être fermée par son délimiteur correspondant `)`, `]`, `}`.
- La fermeture doit respecter l'ordre d'imbrication (une fermeture doit correspondre à
  l'ouverture la plus récente non fermée).
- Une chaîne sans délimiteur (ou vide) est considérée comme équilibrée (`True`).

## Exemples

```python
is_balanced("()")                # True
is_balanced("()[]{}")            # True
is_balanced("({[]})")            # True
is_balanced("(]")                # False
is_balanced("([)]")              # False
is_balanced("((())")            # False  (3 ouvertures, 2 fermetures)
is_balanced("")                  # True
is_balanced("abc")               # True  (aucun délimiteur)
```
""").reponse
)