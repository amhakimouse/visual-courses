### Concept : Classe & Objet

Une **classe** est un plan (blueprint). Un **objet** est une instance concrète créée à partir de ce plan.

```
┌─────────────────────────────┐
│        CLASSE: Utilisateur   │   ← le moule / le plan
│───────────────────────────── │
│ Attributs :                  │
│   - nom                      │
│   - email                    │
│   - motDePasse                │
│───────────────────────────── │
│ Méthodes :                   │
│   - seConnecter()             │
│   - afficherProfil()          │
└─────────────────────────────┘
              │
              │  new Utilisateur(...)
              ▼
   ┌──────────────┐   ┌──────────────┐
   │ OBJET 1       │   │ OBJET 2       │
   │ nom: "Hakim"  │   │ nom: "Sara"   │
   │ email: h@..   │   │ email: s@..   │
   └──────────────┘   └──────────────┘
```

Chaque objet a **ses propres valeurs**, mais **partage la même structure** définie par la classe.

---

### 💻 Exemple pratique : app desktop de gestion d'utilisateurs (type Swing/JavaFX)

java

```java
public class Utilisateur {
    // --- Attributs (état de l'objet) ---
    private String nom;        // stocke le nom de l'utilisateur connecté
    private String email;      // stocke l'email, utilisé comme identifiant unique
    private String motDePasse; // stocke le mot de passe (privé pour sécurité)

    // --- Constructeur : appelé quand on crée un objet avec "new" ---
    public Utilisateur(String nom, String email, String motDePasse) {
        this.nom = nom;               // "this.nom" = attribut de la classe
        this.email = email;           // "email" (paramètre) = valeur reçue
        this.motDePasse = motDePasse; // on initialise l'état de l'objet
    }

    // --- Méthode : comportement de l'objet ---
    public boolean seConnecter(String emailSaisi, String mdpSaisi) {
        // compare les valeurs saisies dans l'interface avec celles stockées
        return this.email.equals(emailSaisi) && this.motDePasse.equals(mdpSaisi);
    }

    public void afficherProfil() {
        // méthode utilisée pour remplir un JLabel ou un champ texte dans l'UI
        System.out.println("Nom: " + nom + " | Email: " + email);
    }
}
```

java

```java
public class Main {
    public static void main(String[] args) {
        // Création de deux OBJETS différents à partir de la MÊME classe
        Utilisateur user1 = new Utilisateur("Hakim", "hakim@app.com", "1234");
        Utilisateur user2 = new Utilisateur("Sara", "sara@app.com", "abcd");

        // Chaque objet garde son propre état, indépendant de l'autre
        user1.afficherProfil(); // → Nom: Hakim | Email: hakim@app.com
        user2.afficherProfil(); // → Nom: Sara | Email: sara@app.com

        // Utilisation typique dans une app desktop : vérifier un login
        boolean connecte = user1.seConnecter("hakim@app.com", "1234");
        System.out.println("Connexion réussie ? " + connecte); // true
    }
}
```

---

#### 📌 À retenir

- **Classe** = plan/modèle → n'existe pas en mémoire tant qu'on ne l'instancie pas.
- **Objet** = instance réelle en mémoire, créée avec `new`.
- Dans une app desktop, chaque fenêtre/formulaire manipule généralement des **objets** (ex: un objet `Utilisateur` connecté, un objet `Produit` sélectionné, etc.).


# Encapsulation

---

### 🎯 Définition

L'encapsulation = **cacher les attributs** (les rendre `private`) et n'autoriser l'accès/modification qu'à travers des **méthodes contrôlées** (`getters`/`setters`).

Le but : empêcher qu'un code extérieur mette l'objet dans un **état invalide**.

```
┌───────────────────────────────────┐
│         CLASSE: CompteBancaire      │
│                                     │
│   🔒 private solde                  │   ← inaccessible directement
│                                     │
│   ┌───────────────────────────┐    │
│   │  🚪 getSolde()             │    │   ← porte d'entrée contrôlée
│   │  🚪 deposer(montant)       │    │   ← vérifie avant de modifier
│   │  🚪 retirer(montant)       │    │   ← refuse si montant invalide
│   └───────────────────────────┘    │
└───────────────────────────────────┘

   Code extérieur :
   compte.solde = -5000;      ❌ IMPOSSIBLE (private)
   compte.retirer(-5000);     ✅ possible, mais la méthode peut REFUSER
```

Sans encapsulation, n'importe quelle partie de l'app pourrait faire `solde = -9999`. Avec encapsulation, seule la méthode `retirer()` décide si c'est autorisé.

---

### 💻 Exemple pratique : app desktop bancaire (JavaFX/Swing)

java

```java
public class CompteBancaire {
    // --- Attribut PRIVÉ : personne à l'extérieur ne peut y toucher directement ---
    private double solde;
    private String titulaire;

    // --- Constructeur ---
    public CompteBancaire(String titulaire, double soldeInitial) {
        this.titulaire = titulaire;
        this.solde = soldeInitial; // état initial fixé une seule fois ici
    }

    // --- Getter : lecture contrôlée de l'attribut privé ---
    public double getSolde() {
        return solde; // on autorise à LIRE le solde (ex: pour l'afficher dans un JLabel)
    }

    // --- Setter avec VALIDATION : c'est là toute la puissance de l'encapsulation ---
    public void deposer(double montant) {
        if (montant > 0) {          // on protège contre une valeur absurde
            this.solde += montant;  // modification uniquement si valide
        } else {
            System.out.println("Montant invalide !"); // refus silencieux ou exception
        }
    }

    public boolean retirer(double montant) {
        if (montant > 0 && montant <= solde) { // vérifie fonds suffisants
            this.solde -= montant;
            return true; // succès → l'UI peut afficher "Retrait effectué"
        }
        return false; // échec → l'UI peut afficher "Solde insuffisant"
    }
}
```

java

```java
public class Main {
    public static void main(String[] args) {
        CompteBancaire compte = new CompteBancaire("Hakim", 1000.0);

        // compte.solde = -5000;  ❌ ERREUR DE COMPILATION : solde est private

        compte.deposer(500);              // dépôt valide → solde = 1500
        boolean ok = compte.retirer(2000); // retrait refusé (dépasse le solde)

        // L'UI (JLabel, TextField...) utilise le getter, jamais l'attribut direct
        System.out.println("Solde actuel : " + compte.getSolde()); // 1500.0
        System.out.println("Retrait réussi ? " + ok); // false
    }
}
```

---

#### 📌 À retenir

- `private` = attribut invisible depuis l'extérieur de la classe.
- `public` getter/setter = seule porte d'accès, où tu peux **ajouter des règles/validations**.
- Dans une app desktop : ça évite qu'un bug dans un formulaire mette une donnée métier (solde, stock, mot de passe...) dans un état incohérent.

## Héritage (Inheritance)

---

### 🎯 Définition

L'héritage permet à une classe (**sous-classe**) de **réutiliser** les attributs et méthodes d'une autre classe (**superclasse**), tout en pouvant ajouter ou modifier son propre comportement.

Mot-clé : **`extends`**

```
              ┌─────────────────────────┐
              │    CLASSE PARENTE         │
              │       Employe              │
              │─────────────────────────  │
              │ nom, salaireBase           │
              │ calculerSalaire()          │
              └─────────────────────────┘
                    ▲              ▲
                    │ extends      │ extends
        ┌───────────────────┐  ┌───────────────────┐
        │  Developpeur        │  │  Manager             │
        │──────────────────── │  │──────────────────── │
        │ langageFavori        │  │ nbEquipe              │
        │ (hérite de nom,      │  │ (hérite de nom,       │
        │  salaireBase,        │  │  salaireBase,          │
        │  calculerSalaire)    │  │  calculerSalaire)      │
        └───────────────────┘  └───────────────────┘
```

`Developpeur` et `Manager` **héritent automatiquement** de tout ce qui est `public`/`protected` dans `Employe`, sans avoir à le réécrire.

---

### 💻 Exemple pratique : app desktop de gestion RH (Swing/JavaFX)

java

```java
// --- CLASSE PARENTE (superclasse) ---
public class Employe {
    protected String nom;         // "protected" = accessible aux sous-classes (pas juste private)
    protected double salaireBase; // attribut commun à TOUS les employés

    public Employe(String nom, double salaireBase) {
        this.nom = nom;
        this.salaireBase = salaireBase;
    }

    // méthode que toutes les sous-classes vont hériter
    public double calculerSalaire() {
        return salaireBase; // comportement par défaut
    }

    public String getNom() {
        return nom; // utilisé pour afficher le nom dans une JTable
    }
}
```

java

```java
// --- SOUS-CLASSE : hérite d'Employe via "extends" ---
public class Developpeur extends Employe {
    private String langageFavori; // attribut propre à Developpeur uniquement

    public Developpeur(String nom, double salaireBase, String langageFavori) {
        super(nom, salaireBase);       // appelle le constructeur de Employe (obligatoire en premier)
        this.langageFavori = langageFavori; // initialise l'attribut spécifique
    }

    // redéfinit (override) le comportement hérité
    @Override
    public double calculerSalaire() {
        return salaireBase + 500; // prime technique ajoutée au salaire de base
    }
}
```

java

```java
// --- AUTRE SOUS-CLASSE : hérite aussi d'Employe ---
public class Manager extends Employe {
    private int nbEquipe;

    public Manager(String nom, double salaireBase, int nbEquipe) {
        super(nom, salaireBase); // réutilise le constructeur parent
        this.nbEquipe = nbEquipe;
    }

    @Override
    public double calculerSalaire() {
        return salaireBase + (nbEquipe * 100); // prime selon taille d'équipe
    }
}
```

java

```java
public class Main {
    public static void main(String[] args) {
        Developpeur dev = new Developpeur("Hakim", 6000, "Java");
        Manager manager = new Manager("Sara", 8000, 5);

        // Chaque objet utilise SA propre version de calculerSalaire()
        System.out.println(dev.getNom() + " → " + dev.calculerSalaire());       // 6500.0
        System.out.println(manager.getNom() + " → " + manager.calculerSalaire()); // 8500.0

        // getNom() est hérité tel quel de Employe, pas besoin de le réécrire
    }
}
```

---

#### 📌 À retenir

- `extends` = "est un(e)" (`Developpeur` **est un** `Employe`).
- `super(...)` = appelle le constructeur de la classe parente — **toujours en 1ère ligne** du constructeur enfant.
- `protected` = accessible dans la classe **et** ses sous-classes (contrairement à `private`).
- Dans une app desktop : idéal pour des hiérarchies comme `Employe` → `Developpeur`/`Manager`, ou `Forme` → `Cercle`/`Rectangle` dans un éditeur graphique.


## Polymorphisme

---

### 🎯 Définition

Le polymorphisme = **une même méthode appelée sur des objets différents produit des comportements différents**, selon le type réel de l'objet — même si on les manipule tous via le type parent.

Deux formes principales :

- **Polymorphisme d'héritage (runtime)** → via `@Override`
- **Surcharge (overloading)** → même nom de méthode, paramètres différents

```
   Employe[] equipe = { dev, manager, dev2 }
              │
              ▼
   ┌─────────────────────────────────────────┐
   │  for (Employe e : equipe)                 │
   │      e.calculerSalaire();                  │
   └─────────────────────────────────────────┘
        │              │              │
        ▼              ▼              ▼
  Developpeur      Manager        Developpeur
  → +500 prime    → +100/pers    → +500 prime

   MÊME appel de méthode → comportement DIFFÉRENT
   selon le VRAI type de l'objet en mémoire
```

Le code appelant (`e.calculerSalaire()`) ne sait même pas s'il manipule un `Developpeur` ou un `Manager` — Java choisit **automatiquement** la bonne version à l'exécution.

---

### 💻 Exemple pratique : app desktop RH — traiter une liste d'employés

On réutilise les classes `Employe`, `Developpeur`, `Manager` du concept précédent.

java

```java
public class Main {
    public static void main(String[] args) {
        // --- Polymorphisme : tableau de type PARENT contenant des objets ENFANTS ---
        Employe[] equipe = {
            new Developpeur("Hakim", 6000, "Java"),  // stocké comme "Employe" mais reste un Developpeur
            new Manager("Sara", 8000, 5),             // stocké comme "Employe" mais reste un Manager
            new Developpeur("Yassine", 5500, "Python")
        };

        // --- Une SEULE boucle, un SEUL appel de méthode, mais résultats différents ---
        for (Employe e : equipe) {
            // Java regarde le type RÉEL de l'objet en mémoire à l'exécution
            // et appelle SA version de calculerSalaire() (pas celle d'Employe)
            System.out.println(e.getNom() + " : " + e.calculerSalaire() + " DH");
        }
        // → Hakim : 6500.0 DH
        // → Sara : 8500.0 DH
        // → Yassine : 6000.0 DH

        // Utile dans une app desktop : une JTable qui affiche une liste
        // mixte d'employés sans savoir/tester leur type exact un par un
    }
}
```

#### Deuxième forme : surcharge (overloading) — utile pour l'UI

java

```java
public class Notification {
    // --- Même nom "envoyer", mais signatures différentes ---
    public void envoyer(String message) {
        System.out.println("SMS : " + message); // ex: notif simple depuis un bouton
    }

    public void envoyer(String message, String destinataire) {
        System.out.println("Email à " + destinataire + " : " + message); // ex: notif ciblée
    }

    public void envoyer(String message, boolean urgent) {
        // ex: une checkbox "urgent" cochée dans un formulaire change le comportement
        System.out.println((urgent ? "🚨 URGENT: " : "") + message);
    }
}
```

java

```java
Notification notif = new Notification();
notif.envoyer("Maintenance prévue");                     // → SMS : Maintenance prévue
notif.envoyer("Facture prête", "client@app.com");         // → Email à client@app.com : Facture prête
notif.envoyer("Serveur down", true);                       // → 🚨 URGENT: Serveur down
```

---

#### 📌 À retenir

- **Override (runtime)** : la méthode appelée dépend du **type réel** de l'objet, pas du type déclaré.
- **Overload (compile-time)** : le compilateur choisit la méthode selon le **nombre/type des paramètres** passés.
- Dans une app desktop : très utile pour traiter des listes hétérogènes (`Forme[]`, `Employe[]`, `Produit[]`) avec un code **unique et générique**, ou pour offrir plusieurs façons d'appeler une même action UI.

## Abstraction

---

### 🎯 Définition

L'abstraction = définir **ce qu'une classe doit faire**, sans dire **comment** elle le fait — en laissant chaque sous-classe implémenter les détails.

Deux outils en Java :

- **Classe abstraite** (`abstract class`) → peut mélanger méthodes concrètes + méthodes obligatoires à implémenter
- **Interface** (`interface`) → contrat pur, que des méthodes à implémenter (+ parfois des constantes)

```
        ┌─────────────────────────────────────┐
        │   abstract class Forme                │
        │───────────────────────────────────── │
        │  ⚙️ couleur (attribut concret)         │
        │  ⚙️ afficherCouleur() → CODE ÉCRIT      │
        │  ❓ calculerAire() → PAS de code,       │
        │      juste la SIGNATURE obligatoire     │
        └─────────────────────────────────────┘
                  ▲                  ▲
                  │                  │
        ┌──────────────────┐  ┌──────────────────┐
        │  Cercle             │  │  Rectangle         │
        │  calculerAire() {   │  │  calculerAire() {   │
        │    π × r²            │  │    largeur × hauteur │
        │  }                   │  │  }                   │
        └──────────────────┘  └──────────────────┘

   ❌ new Forme()  → IMPOSSIBLE (trop abstrait, incomplet)
   ✅ new Cercle() → possible (implémentation complète)
```

Impossible d'instancier `Forme` directement — elle n'est qu'un **modèle incomplet** que les sous-classes doivent compléter.

---

### 💻 Exemple pratique : app desktop — éditeur de formes géométriques (Canvas Swing/JavaFX)

java

```java
// --- CLASSE ABSTRAITE : modèle incomplet, jamais instanciée directement ---
public abstract class Forme {
    protected String couleur; // attribut normal, hérité par toutes les formes

    public Forme(String couleur) {
        this.couleur = couleur;
    }

    // méthode CONCRÈTE : comportement commun, déjà écrit
    public void afficherCouleur() {
        System.out.println("Couleur : " + couleur); // utilisé tel quel par toutes les formes
    }

    // méthode ABSTRAITE : pas de corps, CHAQUE sous-classe DOIT l'écrire
    public abstract double calculerAire();

    // méthode ABSTRAITE aussi : force chaque forme à savoir se dessiner
    public abstract void dessiner();
}
```

java

```java
// --- Implémentation concrète n°1 ---
public class Cercle extends Forme {
    private double rayon;

    public Cercle(String couleur, double rayon) {
        super(couleur);       // initialise l'attribut hérité "couleur"
        this.rayon = rayon;
    }

    @Override
    public double calculerAire() {
        return Math.PI * rayon * rayon; // formule spécifique au cercle
    }

    @Override
    public void dessiner() {
        // ici, dans une vraie app : g.fillOval(...) sur un Canvas/Graphics
        System.out.println("Dessine un cercle de rayon " + rayon);
    }
}
```

java

```java
// --- Implémentation concrète n°2 ---
public class Rectangle extends Forme {
    private double largeur, hauteur;

    public Rectangle(String couleur, double largeur, double hauteur) {
        super(couleur);
        this.largeur = largeur;
        this.hauteur = hauteur;
    }

    @Override
    public double calculerAire() {
        return largeur * hauteur; // formule spécifique au rectangle
    }

    @Override
    public void dessiner() {
        // ici : g.fillRect(...) sur un Canvas/Graphics
        System.out.println("Dessine un rectangle " + largeur + "x" + hauteur);
    }
}
```

java

```java
public class Main {
    public static void main(String[] args) {
        // Forme forme = new Forme("rouge"); ❌ ERREUR : classe abstraite non instanciable

        // On manipule les objets via le type abstrait "Forme" (polymorphisme + abstraction)
        Forme[] formes = {
            new Cercle("Rouge", 5),
            new Rectangle("Bleu", 4, 6)
        };

        for (Forme f : formes) {
            f.afficherCouleur();                          // méthode héritée, identique pour toutes
            f.dessiner();                                  // chaque forme dessine différemment
            System.out.println("Aire : " + f.calculerAire()); // chaque forme calcule différemment
        }
    }
}
```

---

#### 📌 À retenir

- `abstract class` = ne peut **jamais** être instanciée avec `new`.
- Une méthode `abstract` **n'a pas de corps** `{ }` — elle oblige chaque sous-classe à fournir sa propre implémentation.
- Différence clé avec l'héritage simple (Concept 3) : ici, la classe parente **force** l'implémentation au lieu de juste offrir un comportement par défaut réutilisable.
- Dans une app desktop : parfait pour un éditeur graphique (`Forme`), un système de plugins (`Action`), ou tout composant où chaque variante **doit** définir son propre comportement. 