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
        question="""
    # Regroupement d'anagrammes

Implémentez une fonction :

```python
def group_anagrams(words) -> list:
```

qui reçoit une liste de chaînes et renvoie une liste de groupes : chacun contient les mots qui
sont des anagrammes les uns des autres (mêmes lettres, même nombre d'occurrences, casse
insensible).

Règles précises :
- Deux mots sont des anagrammes s'ils ont exactement les mêmes lettres avec les mêmes
  fréquences, en ignorant la casse (`"Tea"` et `"eat"` sont des anagrammes).
- La comparaison doit ignorer la casse, mais les mots du groupe sont renvoyés **tels quels**
  (casse d'origine préservée).
- L'ordre des groupes et l'ordre des mots dans chaque groupe ont la liberté : les résultats ne
  sont vérifiés que comme ensembles de groupes.
- Les chaînes non vides n'ont que des caractères alphabétiques.

## Exemples

```python
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# ex. [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
group_anagrams([])                       # []
group_anagrams(["abc"])                  # [["abc"]]
group_anagrams(["Tea", "ate", "EAT"])    # ex. [["Tea", "ate", "EAT"]]
```

## Dernière implémentation

```python
from collections import defaultdict

def group_anagrams(words) -> list:
    anagram_groups = defaultdict(list)

    for word in words:
        # Convertir le mot en minuscule pour normaliser la comparaison
        key = word.lower()
        anagram_groups[key].append(word)

    # Convertir les valeurs en liste de listes
    return list(anagram_groups.values())
```

Cette implémentation n'a pas passé tous les tests.
Voici les tests échoués:
```python
result = normalize(group_anagrams(["Tea", "ate", "EAT"]))
expected = normalize([["Tea", "ate", "EAT"]])
assert result == expected

result = normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
expected = normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
assert result == expected
``` 

""").reponse
)