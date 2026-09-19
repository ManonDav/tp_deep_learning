# Rapport — Chaînage de prompts et gestion du contexte

## 1. Étape 1 : implémentation directe

L'objectif de cette première étape était d'évaluer la capacité du LLM à résoudre directement les 16 problèmes du banc de tests, sans boucle de correction.

Pour chaque tâche, le harnais récupère la spécification du problème, l'envoie au LLM afin de générer une implémentation Python, puis soumet cette implémentation à l'évaluateur fourni. Le résultat des tests permet ensuite de déterminer si l'implémentation est valide.

La génération en one-shot des 16 fonctions a obtenu le résultat suivant :

**Score : 81,25 %**

**Tâches échouées :**

* `11_group_anagrams`
* `12_word_frequencies`
* `14_parse_csv_line`

Le LLM a donc réussi **13 tâches sur 16**, mais a rencontré des difficultés sur trois problèmes. Ces trois tâches ont été utilisées pour l'étape 2 afin d'expérimenter différentes stratégies de correction.

## 2. Étape 2 : correction à partir du retour des tests

Pour cette deuxième étape, le principe était de transmettre au LLM davantage de contexte lorsqu'une implémentation échouait : la spécification du problème, le code généré, ainsi que les erreurs retournées par les tests.

J'ai choisi de limiter le nombre de tentatives de correction à **5** afin d'éviter une boucle trop importante d'appels au LLM.

### 2.1. Problème 12 — `word_frequencies`

Pour cette première expérimentation, j'ai modifié le prompt afin de transmettre au LLM le code qu'il avait généré, en précisant que celui-ci était incorrect. J'ai également ajouté les tests qui échouaient ainsi qu'une indication générale sur la nature du problème.

Cette modification a permis au LLM de comprendre son erreur et de modifier correctement son implémentation.

Le nouveau résultat est :

**Score : 87,50 %**

**Tâches échouées :**

* `11_group_anagrams`
* `14_parse_csv_line`

Le retour des tests a donc permis de résoudre le problème 12 et d'améliorer le score global de **81,25 % à 87,50 %**.

### 2.2. Problème 11 — `group_anagrams`

J'ai ensuite appliqué une stratégie similaire au problème 11. Le prompt contenait le code généré précédemment, les erreurs des tests et une indication destinée à orienter le LLM vers une correction.

Lors de cette première tentative, le LLM a modifié son programme, mais la nouvelle implémentation échouait encore aux tests.

Le score est donc resté :

**Score : 87,50 %**

**Tâches échouées :**

* `11_group_anagrams`
* `14_parse_csv_line`

J'ai alors formulé une hypothèse : le simple retour des erreurs n'était peut-être pas suffisant pour permettre au modèle d'identifier précisément la cause de son erreur.

J'ai donc modifié le prompt en donnant une explication plus détaillée du problème. J'ai notamment expliqué **pourquoi l'algorithme utilisé était incorrect, ce qui était attendu par les tests et quelle méthodologie pouvait être utilisée pour construire une clé permettant de regrouper correctement les éléments**.

Cette fois, le LLM a produit une implémentation correcte et tous les tests du problème 11 ont été validés.

Le score global est alors passé à :

**Score : 93,75 %**

**Tâches échouées :**

* `14_parse_csv_line`

Cette expérimentation montre que le retour d'erreur peut être utile, mais qu'un feedback plus explicite peut être nécessaire lorsque le modèle ne parvient pas à interpréter correctement la cause de l'échec.

### 2.3. Problème 14 — `parse_csv_line`

Le problème 14 s'est révélé plus difficile à corriger automatiquement.

Comme pour les problèmes précédents, j'ai commencé par modifier le prompt afin de transmettre au LLM :

* la spécification du problème ;
* son implémentation actuelle ;
* les tests échoués ;
* une indication sur ce qu'il devait modifier.

Lors de cette première tentative, le LLM a modifié son code, mais celui-ci échouait toujours aux tests.

Le score est donc resté égale à **93,75 %**.

J'ai ensuite essayé de fournir une explication plus détaillée de l'erreur, en décrivant les différents cas à prendre en compte dans le traitement des guillemets. Cette fois, je n'ai volontairement pas ajouté d'exemples afin de ne pas rendre le prompt inutilement long.

Malgré cela, le LLM n'a quasiment pas modifié son implémentation : seul un commentaire a été changé. Le code restait donc incorrect.

Le score est resté : **93,75 %**.

**Tâche échouée :**

* `14_parse_csv_line`

J'ai ensuite essayé une troisième stratégie en ajoutant des exemples afin d'expliquer plus concrètement les comportements attendus, notamment pour les champs contenant des guillemets et pour les guillemets doubles.

Cependant, le LLM a de nouveau conservé pratiquement le même algorithme et n'a modifié que des éléments secondaires, notamment un commentaire. Les tests échouaient toujours.

Le score est donc resté : **93,75 %**.

Pour la dernière tentative, j'ai finalement simplifié le prompt. L'objectif était de supprimer les explications qui n'avaient pas eu d'effet lors des essais précédents et de mettre davantage l'accent sur une consigne précise : **le code actuel est incorrect et doit réellement être modifié ; il ne doit pas être simplement recopié**.

Cette fois, le LLM a effectivement modifié son code, mais la nouvelle version ne passait toujours pas l'ensemble des tests.

Après les différentes tentatives de correction, le problème 14 reste donc en échec.

**Résultat final de l'étape 2 :**

**Score : 93,75 %**

**Tâche échouée :**

* `14_parse_csv_line`

## 3. Impact du réessai et du retour d'erreur

Au cours des expérimentations, j'ai également testé le comportement du LLM lorsqu'on relance exactement le même prompt.

À chaque étape de correction, j'ai commencé par relancer le script sans modifier le prompt. Dans un cas sur trois, le code généré a légèrement changé, mais cette nouvelle version ne passait toujours pas les tests. Dans les deux autres cas, la réponse produite était identique.

Cela montre que **relancer simplement le même prompt offre peu de chances d'améliorer significativement le résultat**.

À l'inverse, l'ajout du retour des tests a permis d'obtenir des modifications du programme. Dans le cas du problème 12, ce retour a directement permis d'obtenir une implémentation correcte. Pour le problème 11, le simple retour d'erreur n'a pas été suffisant, mais l'ajout d'une explication plus détaillée a permis de résoudre le problème.

Le retour des tests constitue donc un élément important du contexte transmis au LLM : il permet de transformer une génération one-shot en un processus itératif dans lequel le modèle peut essayer de corriger son implémentation.

## 4. Exploration des stratégies de prompt

Les différentes expérimentations ont principalement porté sur la quantité et la nature des informations fournies au LLM.

J'ai testé plusieurs niveaux de feedback :

1. **Prompt initial sans retour des tests**
   Le LLM génère directement une solution à partir de la spécification.

2. **Ajout du code incorrect et des erreurs des tests**
   Le modèle dispose alors de davantage de contexte et sait précisément que son implémentation précédente n'est pas valide.

3. **Ajout d'une explication de l'erreur**
   Lorsque le simple retour des tests n'était pas suffisant, j'ai expliqué pourquoi l'algorithme utilisé était incorrect et quelle approche générale devait être suivie.

4. **Ajout d'exemples**
   Pour le problème 14, j'ai essayé d'expliciter certains comportements attendus à l'aide d'exemples.

5. **Simplification du prompt**
   Enfin, j'ai réduit les explications afin de conserver uniquement les informations essentielles et de demander explicitement au modèle de modifier son code plutôt que de le recopier.

Ces expérimentations montrent qu'**augmenter la quantité de contexte ne garantit pas nécessairement une meilleure correction**. Dans le cas du problème 11, une explication plus détaillée a été efficace. En revanche, pour le problème 14, l'ajout d'informations supplémentaires n'a pas permis au modèle de produire une solution correcte.

## 5. Résultats et nombre d'appels au LLM

L'étape 1 a permis d'obtenir un taux de réussite de : **81,25 %**.

Après la mise en place de la correction itérative et des différentes stratégies de prompt, le meilleur résultat obtenu est : **93,75 %**.

La boucle de correction a donc permis de résoudre **2 des 3 problèmes initialement en échec**, soit une amélioration de **12,5 points de pourcentage**.

Le nombre moyen d'appels au LLM sur l'ensemble du banc de tâches est de **1,4375 appel par tâche**.

## 6. Conclusion

La correction automatique par chaînage de prompts a permis d'améliorer significativement les performances du LLM. Le taux de réussite est passé de **81,25 % à 93,75 %**, avec seulement une tâche restant en échec après les différentes tentatives.

Les expérimentations montrent tout d'abord que **relancer un prompt identique est peu efficace**. Même lorsque le modèle génère une réponse légèrement différente, celle-ci ne corrige généralement pas le problème initial.

En revanche, **fournir au LLM le retour des tests permet d'améliorer le processus de génération**. Le modèle sait alors que son implémentation est incorrecte et dispose d'informations supplémentaires pour tenter de la corriger. Cette stratégie a notamment permis de résoudre directement le problème 12.

Cependant, le niveau de détail du feedback doit être adapté au problème. Pour le problème 11, une explication plus précise de l'erreur a permis de débloquer la correction. À l'inverse, pour le problème 14, l'ajout d'explications et d'exemples n'a pas suffi.

Le problème `14_parse_csv_line` reste donc en échec après plusieurs tentatives. Je pense que cette difficulté vient notamment de la gestion des guillemets et des guillemets doubles, qui nécessite de respecter plusieurs règles simultanément. Le prompt devient également plus volumineux car la fonction et sa spécification sont elles-mêmes assez longues. Les différentes tentatives montrent que le modèle peut parfois rester bloqué sur son algorithme initial et se contenter de modifier des éléments superficiels, comme des commentaires, malgré un retour indiquant clairement que les tests échouent.

Cette expérimentation met ainsi en évidence une limite importante de la correction automatique : **fournir davantage de contexte ne garantit pas que le modèle identifiera la cause réelle de son erreur**. Il peut être nécessaire d'adapter la stratégie de prompting au problème rencontré, mais il n'est pas toujours possible de déterminer précisément quelle information permettra au modèle de débloquer la situation.

Malgré cette limite, le chaînage de prompts et l'utilisation du retour des tests constituent une amélioration intéressante par rapport à une génération one-shot. Ils permettent au LLM d'exploiter les résultats de son propre code et d'effectuer plusieurs tentatives de correction, ce qui a permis dans notre cas de passer de **13/16 à 15/16 tâches réussies**.
