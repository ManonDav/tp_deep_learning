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
        question="""# Chiffrement de César

Implémentez une fonction :

```python
def caesar_cipher(s: str, shift: int) -> str:
```

qui chiffre `s` avec un décalage de César de `shift` positions dans l'alphabet (a → z).
`shift` est un entier pouvant être négatif ou supérieur à 25.

Règles précises :
- Seules les lettres de l'alphabet anglais sont décalées. Les autres caractères (espaces,
  chiffres, ponctuation) restent inchangés.
- La casse est préservée : une majuscule reste une majuscule, une minuscule reste une minuscule.
- Le décalage "boucle" sur l'alphabet (modulo 26), y compris pour les valeurs négatives ou
  supérieures à 25.

## Exemples

```python
caesar_cipher("abc", 3)        # "def"
caesar_cipher("xyz", 3)        # "abc"
caesar_cipher("Hello, World!", 1)  # "Ifmmp, Xpsme!"
caesar_cipher("abc", -1)       # "zab"
caesar_cipher("abc", 29)       # "def"  (29 ≡ 3 mod 26)
```
""").reponse
)