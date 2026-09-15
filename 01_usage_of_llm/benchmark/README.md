# Banc de tâches

Ce dossier contient les 16 tâches du TP *Chaînage de prompts et gestion du contexte*.

## Structure

Chaque tâche est un dossier `NN_nom_de_la_tache/` contenant :

- `spec.md` — l'énoncé précis à envoyer au LLM (nom de fonction, signature, comportement attendu, cas limites, exemples). C'est le texte (ou une reformulation fidèle) que votre harnais doit inclure dans le prompt.
- `test_task.py` — les tests unitaires qui valident une implémentation. Ils importent la fonction depuis un module `solution.py` **situé dans le même dossier**.

## Contrat attendu par les tests

Pour chaque tâche :

1. Extraire le code Python généré par le LLM (un seul bloc de code contenant la fonction demandée, avec **exactement** le nom de fonction donné dans `spec.md`).
2. Écrire ce code dans `NN_nom_de_la_tache/solution.py` (écrase le fichier précédent à chaque tentative).
3. Exécuter les tests via le harnais fourni (voir ci-dessous).

Les fichiers `test_task.py` ajoutent eux-mêmes le dossier de la tâche à `sys.path`, donc l'import `from solution import ...` fonctionne quel que soit le répertoire depuis lequel les tests sont lancés.

## Module d'aide `evaluator.py`

Le module `evaluator.py` expose trois fonctions pour piloter le banc depuis votre harnais :

- `get_task_description(task_id)` — renvoie le contenu de `spec.md` de la tâche, c'est-à-dire le
  prompt à envoyer au LLM. `task_id` est soit le nom du dossier (`"07_merge_intervals"`), soit le
  numéro de la tâche (`7`).
- `test_implementation(task_id, code)` — écrit `code` dans `solution.py` de la tâche, exécute ses
  tests unitaires, et renvoie `(valid, message)` : `valid` vaut `True` si tous les tests passent
  (`message` est alors `""`), sinon `False` et `message` contient un rapport d'erreur concis
  (tests en échec + traceback) destiné à être renvoyé au LLM à l'étape 2.
- `score_implementations(implementations)` — teste un lot d'implémentations et renvoie
  `(score, failed)` : `score` est le taux de réussite (float entre `0.0` et `1.0`), `failed` la
  liste triée des identifiants des tâches dont l'implémentation est invalide.

```python
import evaluator

prompt = evaluator.get_task_description("07_merge_intervals")
# ... code = <code généré par le LLM>

valid, report = evaluator.test_implementation("07_merge_intervals", code)

# À l'étape 1, on peut évaluer toutes les tâches d'un coup :
implementations = {task_id: code for task_id, code in ...}
score, failed = evaluator.score_implementations(implementations)
```

## Liste des tâches

| # | Tâche | Fonction | Difficulté indicative |
|---|-------|----------|------------------------|
| 01 | Palindrome | `is_palindrome` | facile / piège de normalisation |
| 02 | Compression RLE | `run_length_encode` | facile |
| 03 | Aplatissement de liste | `flatten` | moyenne (récursion) |
| 04 | Élément le plus fréquent | `most_frequent` | facile / règle d'égalité |
| 05 | Parenthèses équilibrées | `is_balanced` | moyenne |
| 06 | Chiffrement de César | `caesar_cipher` | moyenne (modulo, casse) |
| 07 | Fusion d'intervalles | `merge_intervals` | moyenne / difficile |
| 08 | Romain → entier | `roman_to_int` | moyenne |
| 09 | Entier → romain | `int_to_roman` | moyenne / difficile |
| 10 | Recherche dichotomique | `binary_search` | facile / algorithme imposé |
| 11 | Regroupement d'anagrammes | `group_anagrams` | moyenne |
| 12 | Fréquence des mots | `word_frequencies` | facile / nettoyage de texte |
| 13 | Fibonacci efficace | `fibonacci` | difficile (contrainte de performance) |
| 14 | Analyse d'une ligne CSV | `parse_csv_line` | difficile (guillemets, échappement) |
| 15 | Deux nombres dont la somme est cible | `two_sum` | moyenne / dictionnaire |
| 16 | Préfixe commun le plus long | `longest_common_prefix` | facile / cas limites |

Les tâches 07, 09, 13 et 14 sont volontairement les plus susceptibles de mettre un petit modèle en échec dès la première tentative : gardez-les pour discuter des limites de l'étape 2 dans votre rapport.
