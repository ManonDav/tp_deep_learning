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
        question='''
    # Analyse d'une ligne CSV

Implémentez une fonction :

```python
def parse_csv_line(line: str) -> list:
```

qui découpe une ligne de fichier CSV en une liste de champs (chaînes).

Règles précises :
- Les champs sont séparés par des virgules.
- Un champ peut être entouré de guillemets doubles `"`. Dans ce cas :
  - une virgule ou un retour à la ligne à l'intérieur des guillemets ne termine pas le champ ;
  - deux guillemets consécutifs `""` à l'intérieur d'un champ entre guillemets représentent un
    guillemet littéral dans la valeur.
- Un champ non entre guillemets ne contient pas de guillemets : toute valeur contenant un
  guillemet est entre guillemets.
- Les guillemets qui entourent un champ ne font **pas** partie de la valeur renvoyée.
- Chaque ligne est bien formée (les guillemets ouvrants ont toujours un fermant) : vous n'avez
  pas à gérer les lignes mal formées.
- Une ligne vide ou constituée seulement d'une virgule donne `[""]` ou `["", ""]` : chaque
  position séparée par une virgule donne un champ, même vide.

## Exemples

```python
parse_csv_line("a,b,c")                # ["a", "b", "c"]
parse_csv_line("a,\"b,c\",d")           # ["a", "b,c", "d"]
parse_csv_line("\"hello \"\"world\"\"\"")  # ["hello \"world\""]
parse_csv_line("1,2,3")                # ["1", "2", "3"]
parse_csv_line("a,")                   # ["a", ""]
```
## Dernière implémentation

```python
def parse_csv_line(line: str) -> list:
    if not line:
        return [""]

    fields = []
    i = 0
    n = len(line)
    in_quotes = False
    current_field = ""

    while i < n:
        char = line[i]

        if char == '"':
            if in_quotes:
                # Two quotes in a row represent a single quote in the value
                if i + 1 < n and line[i + 1] == '"':
                    current_field += '"'
                    i += 2
                    continue
                # End of quoted field
                in_quotes = False
                i += 1
            else:
                # Start of quoted field
                in_quotes = True
                i += 1
                continue

        if char == ',' and not in_quotes:
            # End of a field
            fields.append(current_field)
            current_field = ""
            i += 1
        else:
            # Add character to current field
            current_field += char
            i += 1

    # Add the last field
    fields.append(current_field)

    # Handle empty fields (e.g., ",")
    return fields
```
Cette implémentation n'a pas passé tous les tests.
Voici les tests échoués:
```python
assert parse_csv_line(\'"hello ""world"""\') == [\'hello "world"\']
assert parse_csv_line(\'a,"b,c",d\') == ["a", "b,c", "d"]
assert parse_csv_line(\'"  x  "\') == ["  x  "]
assert parse_csv_line(\'""\') == [""]
```
Le problème se situe dans la logique de gestion des guillemets.

Le code actuel est incorrect.
Tu dois modifier son algorithme pour que les tests échoués passent.
Ne recopie pas le code actuel.
Retourne uniquement le code Python corrigé.
''').reponse
)