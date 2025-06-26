# COURS METHODOLOGIE DE TEST

Ici les TP (matin) et certaines activités (aprés-midi) du cours de Ynov sur la méthodologie de tests
- 1 dossier par TP
- 1 dossier par activité à partir de l'activité de la séance 2 : `ActiviteS2`
- Commits par exercices : voir les anciens commits pour retrouver les versions (si il y a des surcharges demadées dans les exercices)

## Activité Séance 2

L'activité séance 2 du vendredi aprés-midi (20/06) à rendre pour le vendredi suivant (27/06) est dans le dossier `ActiviteS2`.

### Activité S2 > Livrables : 

1. Nouvelle version des tests (code) : 
- se trouve dans le sous-dossier:<br> `ActiviteS2/Kata/python_pytest` 
- C'est le zip de la branche main du kata de Emily Batch
- On utilisera la version python avec pytest

2. Rapport de couverture de code (avant/après)
- Captures d'écrans de la couverture initiale des tests dans le dossier:<br> 
  `ActiviteS2/rapports-couverture/avant` [Accés ici](./ActiviteS2/rapports-couverture/avant)<br>

- Captures d'écrans de la couverture aprés mon refactoring : <br> 
  `ActiviteS2/rapports-couverture/apres` [Accés ici](./ActiviteS2/rapports-couverture/apres/rapport_couverture_apres.png)<br>

3. Justification (texte court .md, .txt ou Notion partagé) : 
- Se trouve dans ce fichier : `ActiviteS2/justification.md` [Accés ici](./ActiviteS2/justification.md) <br>

4. Liste des doublures utilisées avec explication
- Se trouve dans ce fichier : `ActiviteS2/list_doublures.md` [Accés ici](./ActiviteS2/list_doublures.md) <br>

## TP2 (MATIN)

Ayant assisté à une partie de la correction du TP2 sur le script de météo, j'ai décidé d'utiliser un autre exercice afin de réaliser quelque-chose de proche en terme de refactoring et mocking pour répondre aux objectifs pédagogique. Cela a plus de crédit.

J'ai choisis le dossier en TypeScript pour varier car python est déjà utilisé sur l'aprés-midi.

En réalité ce jeu de test aurait dû nous être fournit pour l'aprés-midi (cf Clara) mais il y a eu une erreur et la class a travaillé sur le kata de supermarché.

J'en profite donc pour le réutiliser sur les TP du matin.

### Consignes :

#### Questions (issue du TP2 sur la météo et appliqué à ce TP de conversion de monnaie) :
- ***Les questions sont assez similaire pour être appliqué au cas présenté dans ce TP***
- ***Le TP de conversion monnaie possède en effet déjà un problème d'appel API : on le voit lors du premier scan des tests.***

1. Que se passe-t-il si vous n'avez pas internet ?
2. Comment tester le cas où l'API retourne une erreur ?
3. Comment être sûr que votre fonction gère bien les différents cas ?
4. Que doit retourner votre fonction si status_code != 200 ?
5. Comment vérifier que l'appel API a bien été fait ?

**Mocking : faire un refactoring pour se passer de l'accés internet et de l'API**
6. Lancez le test et vérifiez qu'il passe
7. Observez : plus besoin d'internet !

#### Mes réponses : 
Cette exercice est réalisé dans ce dossier : `tp2_mocking_amaury` [Cliquez ici pour accéder](./tp2_mocking_amaury)<br>

Je vous guide dans mes différentes réponses et documents associées aux questions ci-dessus.<br>

> Consulter la capture d'écran `snapshots_states/kata_conversion_first_state.png` : état de base de l'exercice avant tout refactoring.<br>
- [Cliquez ici pour accéder](./tp2_mocking_amaury/snapshots_states/kata_conversion_first_state.png)<br>

1. Que se passe-t-il si vous n'avez pas internet ?<br>
- A ce stade, si l'on répare l'appel API, nous aurions accés à des données issue directement de l'API pour être réutilisé dans nos tests. Or si l'on veut tester en phase de développement sans accés internet et aussi avec de la performance nous avons un problème car aucune donnée ne peut parvenir à nos tests. Les tests vont donc échouer mais ce sera des échec faussés car le problème vient de l'absence de données fiables. Avec de la chance, l'outil de test prévient qu'aucune donnée n'est passé mais avec de la malchance on aurait affaire à des message trop généraux d'erreurs. Aussi nous n'aurions que peu d'information sur l'origine du problème car nous n'avons pas prévu de signaler clairement que le problème vient d'un accés internet défaillant.

2. Comment tester le cas où l'API retourne une erreur ?
- Nous pourrions le faire directement avec les données issu de l'API pour peu qu'on ait internet mais cette réponse est naïve. En effet, les cas issu des données réelles sont souvent variable et dépende d'autres facteurs qui ne permet pas d'isoler nos cas d'erreurs avec aisance. La variabilité empêche le repérage précis des cas d'erreur dans notre base de code et ne permet pas de rendre nos tests déterministe quand la contexte s'y prête (ou de contrôler dans le cas contraire des données aléatoires qui couvre tous les cas limites). On pourra tester des cas nominaux mais on laisse les cas limites à la merci de données non-maîtrisé issu du monde réel. Ainsi nous ne pouvons faire le tour de tous les cas d'erreurs et utiliser avec fiabilité des technique comme la table de vérité (vu qu'on ne sait pas quels sont les données entrantes). Le pire est pour l'application de météo mais le problème se pose aussi ici avec les conversion de monnaies car la monnaie change en fonction des cours des bourses ! 

- La solution consiste donc à créer une simulation d'appel API tout en testant aussi des appel réel pour isoler les cas où c'est l'appel API qui pose problème.

Voici ce que nous pouvons faire pour tester les cas où l'API retourne une erreur: 
- Vérifier que les appel HTTP(S) marche
- Isoler certains appels pour certains cas précis ou des groupe de cas avec une même cause d'erreur
- Vérifier les cas où l'appel ne retourne pas la donnée : donnée inexistante
- Vérifier les cas où l'appel ne trouve pas un fichier : fichier non-trouvé
