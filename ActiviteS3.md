# Activité Séance 3

## Rappel du contexte : 
Vous intégrez une équipe qui teste les fonctionnalités d’une bibliothèque de gestion d’inscriptions à des événements.

## Consignes
1. Implémenter une fonctionalité simple mais réaliste à partir d’un besoin (ex : génération d’un mail de confirmation d’inscription avec résumé des infos)
2. Utiliser la méthode TDD : écriture du test avant, code minimal, refactor
3. Utiliser Approval Testing pour valider le contenu du message ou du fichier généré
4. Générer un fichier d’approbation (golden file ou snapshot selon le framework choisi)

## Ma démarche 

- Framework choisi : NestJs avec Jest en librairie de test (et des outils complémentaires)
- Point de départ, faire un git checkout à ce commit : `ActiviteS3(initial): initial commit on activiteS3`

Je vais documenter commit aprés commit ma démarche TDD sur ce projet.
Le point de départ est une application NestJs minimale qui expose un 'Hello World'.
Nous devons créer une fonctionnalité dans le cadre d'un système d'inscription à des évènements.

### Départ

On va tout d'abord se poser des questions métier pour implémenter avec une logique minimale pour l'exercice : 

Nous n'allons pas implémenter un système d'authentification afin de rester dans la version minimaliste.

Il y a deux acteurs : un organisateur et un utilisateur de la bibliothèque d'évènement.

1. Ajouter un évènement : en tant qu'organisateur je veux ajouter un évènement à la bibliothèque d'évènements
- Actions de l'organisateur : changer les dates, changer le nombre de participants, annuler l'évènement, envoyer un email aux utilisateurs si annulation, changement ou création.
- Pré-requis : seul l'organisateur peut faire les actions ci-dessus.
- Contraintes : doit se faire 6 jours à l'avance et le nombre de places est limité à 1000, 


2. S'inscrire à un évènements : en tant que utilisateur de l'application je veux m'inscrire à des évènements
- Actions : réserver son ticket, annuler sa réservation à un évènement, consulter ses réservations (publiquement car pas de compte).
- Contraintes : vérifier les tickets restants soit < nombre max d'inscris, vérifier qu'un utilisateur n'est pas déjà inscris

3. Utilisateur : Recevoir une confirmation d'inscription 
- Actions: Réception d'une confirmation d'inscription avec le nom de l'évènement, la date, ses coordonnées.
- Contraintes : doit être inscris à un évènement et avoir renseigné un email.

La confirmation écrite sera stockée ici dans un fichier pour l'exercice et pourra faire l'objet d'une démarche d'approval tests.

Evidemment c'est pas trés bien au niveau du RGPD mais pour l'exercice les emails seront rendu publique et nous ne traiterons pas ces cas de sécurisation juridiques.

Pour ce faire nous avons une base de code.

### Etape 1 - Ajouter un évènement 

Nous allons respecter la démarche du TDD pour réaliser un premier cas d'usage : **ajouter un évènement**.<br>

Nous allons creer une structure qui rend le **couplage le plus faible possible** découpé par use-case.<br> 

Nous nous inspirons de l'**architecture hexagonal** pour créer un système trés modulaire.<br>

#### Nous codons un premier pan minimal de la fonctionnalité pour y exercer les 3 phases du TDD
- Commit de référence : `feat(usecases): create minimal add a new event use-case - tdd red phase`

1. Nous allons préparer l'environnement des tests (le premier A de AAA: Arrange)
- Nous créons l'entité Event qui reprend ce dont a besoin un évènement : 

```sh
type EventProps = {
  id: string;
  title: string;
  participants: number;
  startDate: Date;
  endDate: Date;
};

export class Event {
  constructor(public props: EventProps) {}
}
```
- Dans un dossier adapter : nous créons un outil qui va simuler l'appel à une base de donnée fictive pour commencer : `EventRepositoryMocker`.
- Nous créons des interfaces dans un dossier ports afin de respecter la logique d'architecture hexagonal et le Dependency Inversion Principle.
- Dans un dossier usecases : nous créons `add-event.ts` et pour les tests `add-events.test.ts`
- Nous créons des tests avec un `BeforeAll` qui va reprendre des objets et mettre en place l'environnement qui sera repris pat chaque test de cette suite.

2. En TDD, **phase rouge** : nous allons écrire notre tests pour réaliser cette action :
- Notre but est que l'évènement soit sauvegardé en base de donnée
- On écrit donc un test en respectant le AAA et en utilisant ce que nous avons préparé.

Dans le cadre du TDD nous codons un pan minimal mais cohérent et lançons les tests qui vont sûrement échouer. C'est la phase rouge.
L'échec des tests renseigne sur ce qui va manquer à notre fonction pour qu'elle soit au moins fonctionnelle (cas nominal).

Nous avons donc un test qui va : 
- Insérer un évènement en base de donnée en respectant notre domaine (cf structure de l'entité Event)
- Récupérer cette évènement de la base de donnée et son id : c'est là que l'on sait que le test passe
- Dans notre cas, nous avons mocké notre appel à la base de donnée.

Nous avons bel et bien un échec : 
- Le test échoue à récupérer un id
- Le test échoue à récupérer un objet Event issu de la base de donnée

En effet, notre code n'est pas encore implémenté : on a juste un squelette qui vise à ce que les tests n'échoue pas pour une raison non-lié à la fonctionnalité. 

3. TDD - Ajouter un évènement - Faire passer les tests (Phase Green)
Commit concernées : 
- `feat(add-event): retrive an id - test first pass`
- `feat(add-event): cas nominal passe - tdd green phase`
Tout d'abord nous allons faire passer le test pour retourner un id : nous retournons en dur in id dans la fonction et il passe.

Cette fois nous allons coder ce qui manque dans notre class qui créer les évènements. Nous allons créer un évènement en respectant notre entité Event.<br>
Nous auront donc un use-case qui permet de vérifier le cas nominal d'ajout d'un évènement.

Il retournera donc l'event issu de la base de donnée lors de l'appel à celle-ci. 
Il pourra avantageusement utiliser l'adapter qui permet de mocker le comportement avec aisance. Nous avons en effet la possibilité de changer cela aisément grâce à nos interface et l'inversion de dépendance. Il sera aisé de simplement se connecter à un adapter qui appel une véritable base de donnée ensuite.

Voici un extrait de notre méthode : 
```ts
    this.repository.create(
      new Event({
        id,
        title: data.title,
        participants: data.participants,
        startDate: data.startDate,
        endDate: data.endDate,
      }),
    );

    return { id };
  ```
4. Phase du refactor : améliorer le code sans changer le comportement

Dans notre cas, nous devrions ici par exemple : 
- Organiser mieux nos fichiers en créant les ports / adapters
Mais connaissant la structure d'avance nous nous sommes trop précipité au début pour créer l'environnement des tests et avons déjà créer ces séparations.

Alors que reste t-il à refactor dans notre cas ?
- Nous créons une ou plusieurs constantes avec des cas nominal types que l'on peux mettre dans nos tests
Ex: la constante `RANDO_EVENT` est un évènement type pour une randonnée dans le Tarn avec 100 participants maximum.
On pourrait aller plus loin : créer des tests paramétrés qui vont tester différents cas nominaux (nombre de participants, dates différentes ...)

A ce moment l'usage d'un outil comme **WallabyJs** est précieux : il indique partout dans le code si le test en lien avec ce code passe ainsi que sur les tests sans avoir besoin de lancer un `pnpm run test`. Ainsi le moindre changement en phase de refactor indique immédiatement si le test passe ou non par une pastille verte ou rouge et un simple survol avec la souris donne des détails. Dans le cadre d'une démarche de TDD il permet d'aller vite et ne pas perdre le fil de sa pensée en plein travail.

