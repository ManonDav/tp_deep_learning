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
