# III. Diagramme de Séquences — Cours Complet avec Exemples

---

## 1. Définition

Un **diagramme de séquences** est un diagramme UML comportemental qui modélise les **interactions chronologiques** entre les acteurs et les objets d'un système pour réaliser un cas d'utilisation.

Il répond à la question : **"Qui envoie quoi à qui, et dans quel ordre ?"**

> **Analogie** : Imaginez un scénario de cinéma — le diagramme de séquences est le script qui décrit les répliques échangées entre les personnages, dans l'ordre du récit.

### Vue d'ensemble — Structure de base

```mermaid
sequenceDiagram
    actor Acteur as 👤 Acteur (Utilisateur)
    participant Objet1 as Objet1 : ClasseA
    participant Objet2 as Objet2 : ClasseB

    Note over Acteur,Objet2: ⏱️ Le temps s'écoule de haut en bas

    Acteur->>Objet1: message1(arg1)
    activate Objet1
    Note right of Objet1: Période d'activité<br/>(rectangle sur la ligne de vie)
    Objet1->>Objet2: message2(arg2)
    activate Objet2
    Objet2-->>Objet1: valeurRetour
    deactivate Objet2
    Objet1-->>Acteur: résultat
    deactivate Objet1
```

---

## 2. Éléments Constitutifs

### a. Les Lignes de Vie (Lifelines)

Chaque participant possède une **ligne de vie** verticale en pointillés, qui représente son existence dans le temps.

| Élément | Représentation | Rôle |
|---|---|---|
| Acteur | Bonhomme | Déclenche le scénario |
| Objet | Rectangle + ligne pointillée | Traite les messages |
| Période d'activité | Rectangle plein sur la ligne | Durée d'exécution d'une opération |

---

## 3. Types de Messages

### 🔵 Message Synchrone (flèche pleine `—→`)

L'émetteur **se bloque** et attend la fin de l'opération avant de continuer. C'est le type le plus courant (appel de méthode classique).

```mermaid
sequenceDiagram
    actor Client
    participant Serveur

    Note over Client,Serveur: 🔵 Message Synchrone — le client attend la réponse

    Client->>Serveur: authentifier(login, motDePasse)
    activate Serveur
    Note right of Serveur: Le client est bloqué<br/>pendant l'exécution
    Serveur-->>Client: token : "xyz123"
    deactivate Serveur

    Note over Client: ✅ Le client reprend son exécution
```

> **Exemple concret** : Appel d'une API REST — le navigateur attend la réponse du serveur avant d'afficher la page.

---

### 🟢 Message Asynchrone (flèche ouverte `-→`)

L'émetteur **n'attend pas** la réponse et continue immédiatement. Utilisé pour les événements, files de messages, notifications.

```mermaid
sequenceDiagram
    participant AppMobile as 📱 App Mobile
    participant ServeurMail as 📧 Serveur Mail
    participant Utilisateur as 👤 Utilisateur

    Note over AppMobile,Utilisateur: 🟢 Messages Asynchrones — pas d'attente

    AppMobile-)ServeurMail: envoyerEmail(destinataire, contenu)
    Note right of AppMobile: L'app continue sans attendre
    AppMobile-)Utilisateur: afficherNotification("Email envoyé !")
    Note right of ServeurMail: Le serveur traite l'email<br/>en arrière-plan
    ServeurMail-)Utilisateur: notifierReception()
```

> **Exemple concret** : Envoi d'un email — l'application n'attend pas la confirmation de réception pour continuer.

---

### 🟡 Message de Création (`create`) et Destruction (`destroy`)

Un objet peut être **créé dynamiquement** pendant le scénario, et **détruit** en fin de vie.

```mermaid
sequenceDiagram
    actor Admin
    participant Systeme as Système
    participant Panier as 🛒 Panier (nouvel objet)

    Admin->>Systeme: ouvrirSession(userId)
    activate Systeme

    Note over Systeme,Panier: Création dynamique d'un objet Panier
    create participant Panier
    Systeme->>Panier: create(userId)
    activate Panier

    Admin->>Panier: ajouterArticle("Livre Java", 1)
    Panier-->>Admin: articleAjouté : true

    Admin->>Systeme: fermerSession()

    Note over Panier: Destruction de l'objet
    destroy Panier
    Systeme->>Panier: destroy()
    deactivate Panier
    deactivate Systeme
```

> **Exemple concret** : Dans un site e-commerce, le panier est créé à l'ouverture de la session et détruit à la fermeture.

---

### 🔴 Message Réflexif (auto-message)

Un objet s'envoie **un message à lui-même** — il appelle l'une de ses propres méthodes.

```mermaid
sequenceDiagram
    actor Utilisateur
    participant Compte as 💰 Compte

    Utilisateur->>Compte: effectuerVirement(montant, destination)
    activate Compte

    Note right of Compte: L'objet s'appelle lui-même
    Compte->>Compte: verifierSolde(montant)
    activate Compte
    Compte-->>Compte: solde_suffisant : true
    deactivate Compte

    Compte->>Compte: debiter(montant)
    activate Compte
    Compte-->>Compte: ok
    deactivate Compte

    Compte-->>Utilisateur: confirmation : "Virement effectué"
    deactivate Compte
```

> **Exemple concret** : Un objet `Compte` vérifie son propre solde avant d'effectuer un débit.

---

## 4. Les Fragments Combinés

Les fragments combinés permettent de modéliser des **structures de contrôle** (conditions, boucles, options) directement dans le diagramme.

---

### 🔀 Fragment `alt` — Condition (équivalent `if / else if / else`)

Permet de représenter plusieurs chemins d'exécution alternatifs selon des conditions.

```mermaid
sequenceDiagram
    actor Etudiant
    participant SysNotes as 📊 Système de Notes
    participant BD as 🗄️ Base de Données

    Etudiant->>SysNotes: consulterResultat(etudiantId)
    activate SysNotes
    SysNotes->>BD: getNotes(etudiantId)
    BD-->>SysNotes: notes[]

    alt notes >= 16
        SysNotes-->>Etudiant: "Mention Très Bien 🏅"
    else notes >= 14
        SysNotes-->>Etudiant: "Mention Bien 🥈"
    else notes >= 12
        SysNotes-->>Etudiant: "Mention Assez Bien"
    else notes >= 10
        SysNotes-->>Etudiant: "Admis sans mention"
    else
        SysNotes-->>Etudiant: "Ajourné ❌"
    end

    deactivate SysNotes
```

> **Exemple concret** : Affichage du résultat d'un étudiant selon sa moyenne — chaque alternative correspond à une mention différente.

---

### ❓ Fragment `opt` — Option (équivalent `if` sans `else`)

Représente un comportement **facultatif** qui peut ou non se produire selon une condition.

```mermaid
sequenceDiagram
    actor Client
    participant SiteWeb as 🛍️ Site Web
    participant ServiceSMS as 📱 Service SMS

    Client->>SiteWeb: passerCommande(panier)
    activate SiteWeb
    SiteWeb-->>Client: confirmationCommande(numCmd)

    opt client.notificationsActivées == true
        Note over SiteWeb,ServiceSMS: Ce bloc est optionnel
        SiteWeb->>ServiceSMS: envoyerSMS(client.telephone, "Commande confirmée")
        ServiceSMS-->>SiteWeb: smsSent : true
    end

    deactivate SiteWeb
```

> **Exemple concret** : Un SMS de confirmation n'est envoyé **que si** le client a activé les notifications.

---

### 🔁 Fragment `loop` — Boucle

Modélise une répétition d'interactions. On peut préciser la condition de maintien de la boucle ou le nombre d'itérations.

```mermaid
sequenceDiagram
    actor Professeur
    participant Systeme as 📋 Système
    participant BD as 🗄️ BD

    Professeur->>Systeme: saisirNotes(listeEtudiants)
    activate Systeme

    loop Pour chaque étudiant de la liste
        Systeme->>Professeur: demanderNote(etudiant.nom)
        Professeur->>Systeme: saisirNote(etudiant.id, note)
        activate Systeme
        Systeme->>BD: enregistrerNote(etudiant.id, note)
        BD-->>Systeme: success
        Systeme-->>Professeur: "Note enregistrée"
        deactivate Systeme
    end

    Systeme-->>Professeur: "Toutes les notes ont été saisies ✅"
    deactivate Systeme
```

> **Exemple concret** : Un professeur saisit les notes une par une pour chaque étudiant d'une liste.

---

### 🔗 Fragment `ref` — Référence à un autre diagramme

Permet de **factoriser** des comportements communs en référençant un autre diagramme de séquences, allégeant ainsi les diagrammes complexes.

```mermaid
sequenceDiagram
    actor Employe as 👔 Employé
    participant SysRH as 🏢 Système RH
    participant SysPaie as 💳 Système Paie

    Employe->>SysRH: demanderConge(dateDebut, dateFin)
    activate SysRH

    rect rgb(200, 230, 255)
        Note over SysRH: <<ref>> Authentification_SSO
    end

    SysRH->>SysRH: verifierQuotaConges(employe.id)

    alt quota disponible
        SysRH->>SysPaie: notifierAbsence(employe.id, jours)
        SysPaie-->>SysRH: ok
        SysRH-->>Employe: "Congé approuvé ✅"
    else quota insuffisant
        SysRH-->>Employe: "Quota insuffisant ❌"
    end

    deactivate SysRH
```

> **Exemple concret** : Le scénario "Demande de congé" réutilise le diagramme "Authentification SSO" sans le redessiner.

---

## 5. Combinaison de Fragments — Exemple Complet

Il est possible de **combiner plusieurs fragments** dans le même diagramme pour modéliser des scénarios complexes.

```mermaid
sequenceDiagram
    actor Client
    participant AppBanque as 📱 App Banque
    participant Auth as 🔐 Service Auth
    participant Compte as 💰 Compte
    participant BD as 🗄️ Base de Données

    Client->>AppBanque: seConnecter(login, mdp)
    activate AppBanque
    AppBanque->>Auth: verifierCredentials(login, mdp)
    activate Auth

    alt credentials valides
        Auth-->>AppBanque: token_jwt
        deactivate Auth
        AppBanque-->>Client: "Connexion réussie ✅"

        loop Tant que session active (< 30 min)
            Client->>AppBanque: consulterSolde()
            AppBanque->>Compte: getSolde(userId)
            activate Compte
            Compte->>BD: SELECT solde FROM comptes WHERE id=userId
            BD-->>Compte: solde : 1540.00
            Compte-->>AppBanque: solde : 1540.00
            deactivate Compte
            AppBanque-->>Client: afficher(1540.00 EUR)

            opt Client demande un virement
                Client->>AppBanque: effectuerVirement(montant, iban)
                activate AppBanque
                AppBanque->>Compte: virer(montant, iban)
                activate Compte
                Compte->>Compte: verifierSolde(montant)
                Compte->>BD: UPDATE comptes SET solde=solde-montant
                BD-->>Compte: ok
                Compte-->>AppBanque: virementOk
                deactivate Compte
                AppBanque-->>Client: "Virement effectué ✅"
                deactivate AppBanque
            end
        end

    else credentials invalides
        Auth-->>AppBanque: erreur_auth
        deactivate Auth
        AppBanque-->>Client: "Login ou mot de passe incorrect ❌"
    end

    deactivate AppBanque
```

---

## 6. Diagramme de Séquences Système (DSS)

Un **DSS** est une version simplifiée où le système entier est représenté comme **une seule boîte noire**. On ne détaille pas les objets internes — on montre uniquement les échanges entre les acteurs et le système global.

### Quand utiliser un DSS ?
- En **début de conception** pour aller vite
- Pour valider les **interfaces externes** du système
- Pour alléger des diagrammes trop complexes

```mermaid
sequenceDiagram
    actor Admin as 👤 Administrateur
    participant Sys as ⚙️ :Système

    Note over Admin,Sys: DSS — Cas d'utilisation : "Ajouter un Article"

    Admin->>Sys: seConnecter(login, motDePasse)
    Sys-->>Admin: accèsAutorisé()

    Admin->>Sys: consulterCatalogues()
    Sys-->>Admin: listeCatalogues[]

    Admin->>Sys: choisirCatalogue(catalogueId)
    Admin->>Sys: saisirNouvelArticle(nom, prix, description)

    alt article existe déjà
        Sys-->>Admin: erreur("Article déjà existant ❌")
    else article nouveau
        Sys-->>Admin: confirmation("Article ajouté avec succès ✅")
    end
```

---

## 7. Exemple d'Application Complet — Gestion de Catalogue Produits

```mermaid
sequenceDiagram
    actor Admin as 👤 Administrateur
    participant VueCat as 🖥️ VueCatalogue
    participant Cat as 📦 catalogue : Catalogue
    participant Art as 🏷️ article : Article
    participant BD as 🗄️ BD

    Admin->>VueCat: authentifier(login, mdp)
    activate VueCat
    VueCat->>BD: verifierCredentials(login, mdp)
    BD-->>VueCat: adminValide : true
    VueCat-->>Admin: afficherListeCatalogues()
    deactivate VueCat

    Admin->>VueCat: choisirCatalogue(catalogueId)
    activate VueCat
    VueCat->>Cat: getCatalogue(catalogueId)
    activate Cat
    Cat->>BD: SELECT * FROM catalogues WHERE id=catalogueId
    BD-->>Cat: catalogueData
    Cat-->>VueCat: catalogue
    deactivate Cat
    VueCat-->>Admin: afficherFormulaire()
    deactivate VueCat

    Admin->>VueCat: soumettreArticle(nom, prix, description)
    activate VueCat
    VueCat->>Art: create(nom, prix, description)
    activate Art
    Art->>BD: SELECT * FROM articles WHERE nom=nom AND catalogueId=id
    BD-->>Art: résultat

    alt article existe déjà
        Art-->>VueCat: erreur("Article déjà existant")
        VueCat-->>Admin: afficherErreur("❌ Cet article existe déjà dans ce catalogue")
    else article nouveau
        Art->>BD: INSERT INTO articles VALUES (nom, prix, description, catalogueId)
        BD-->>Art: insertionOk
        Art-->>VueCat: articleAjouté : true
        VueCat-->>Admin: afficherConfirmation("✅ Article ajouté avec succès")
    end

    deactivate Art
    deactivate VueCat
```

## 8. Résumé Visuel des Notations

```mermaid
sequenceDiagram
    participant A as Objet A
    participant B as Objet B
    participant C as Objet C (nouveau)

    Note over A,C: 📌 Récapitulatif des notations UML

    A->>B: Message synchrone (flèche pleine)
    B-->>A: Réponse / Retour (flèche pointillée)

    A-)B: Message asynchrone (flèche ouverte)

    Note over A,C: Création → C existe déjà déclaré en haut, simulé via activate
    activate C
    A->>C: create() — Création d'objet (simulée)
    deactivate C

    A->>A: Message réflexif (auto-appel)

    alt [condition vraie]
        A->>B: fragment alt — branche 1
    else [autre condition]
        A->>B: fragment alt — branche 2
    end

    opt [condition optionnelle]
        A->>B: fragment opt
    end

    loop [condition de boucle]
        A->>B: fragment loop
    end

    Note over C: destroy() — Fin de vie simulée par note
```
## 9. Tableau de Synthèse

| Concept | Notation Mermaid | Signification |
|---|---|---|
| Message synchrone | `->>` | Bloquant, attend la réponse |
| Message asynchrone | `-)` | Non bloquant, continue |
| Message de retour | `-->>` | Réponse optionnelle (pointillés) |
| Création d'objet | `create participant` + `->>` | Nouvel objet dynamique |
| Destruction | `destroy` + `->>` | Fin de vie de l'objet |
| Message réflexif | `A->>A:` | L'objet s'appelle lui-même |
| Fragment `alt` | `alt / else / end` | Condition if/else |
| Fragment `opt` | `opt / end` | Condition if sans else |
| Fragment `loop` | `loop / end` | Boucle |
| Fragment `ref` | `rect` (simulation) | Référence à un autre DS |
| DSS | Système = boîte unique | Vue externe simplifiée |

---
# Diagramme de Séquences — Cas d'Utilisation : "Accès Sécurisé à un ATM"

## Contexte et Analyse

**Système** : Guichet Automatique Bancaire (ATM)  
**Acteurs** :
- 👤 **Client** : insère sa carte et saisit son code

**Classes du système identifiées** :
- `ATM` — Interface du guichet (écran + lecteur carte)
- `Carte` — Entité représentant la carte bancaire
- `BD` — Base de données bancaire (vérification carte et code)

---

## Identification des Fragments

| Situation | Fragment UML |
|---|---|
| Carte valide ou non | `alt` |
| Mauvais code → réessayer (max 3 tentatives) | `loop` (max 3) |
| Code correct ou 3 échecs | `alt` imbriqué dans le `loop` |

---

## Diagramme de Séquences Système (DSS)

```mermaid
sequenceDiagram
    actor Client as 👤 Client
    participant Sys as ⚙️ :ATM

    Client->>Sys: insererCarte()

    alt carte invalide
        Sys-->>Client: ejecterCarte("❌ Carte invalide")
    else carte valide
        Sys-->>Client: demanderCode()

        loop 3 tentatives maximum
            Client->>Sys: saisirCode(code)

            alt code correct
                Sys-->>Client: accesAutorise("✅ Bienvenue")
                Sys-->>Client: afficherMenu()
            else code incorrect et tentatives restantes
                Sys-->>Client: demanderCode("❌ Code erroné, réessayez")
            else code incorrect et 3ème échec
                Sys-->>Client: avalerCarte("🚫 Carte confisquée")
            end
        end
    end
```

---

## Diagramme de Séquences Détaillé

```mermaid
sequenceDiagram
    actor Client as 👤 Client
    participant ATM as 🏧 ATM
    participant Carte as 💳 carte : Carte
    participant BD as 🗄️ BD

    Note over Client,BD: Étape 1 — Insertion et vérification de la carte

    Client->>ATM: insererCarte()
    activate ATM

    ATM->>Carte: lireCarte()
    activate Carte
    Carte->>BD: SELECT * FROM cartes WHERE numero=carteId AND statut='active'
    BD-->>Carte: resultat

    alt carte invalide (expirée, bloquée ou inconnue)
        Carte-->>ATM: carteInvalide
        deactivate Carte
        ATM-->>Client: ejecterCarte("❌ Carte invalide, veuillez contacter votre banque")
        deactivate ATM

    else carte valide
        Carte-->>ATM: carteValide
        deactivate Carte

        Note over Client,BD: Étape 2 — Saisie du code PIN (3 tentatives max)

        ATM-->>Client: afficherEcranCode("Veuillez saisir votre code PIN")

        loop max 3 tentatives [tentative <= 3]

            Client->>ATM: saisirCode(codeSaisi)
            activate ATM
            ATM->>BD: verifierCode(carteId, hash(codeSaisi))
            BD-->>ATM: resultat

            alt code correct
                ATM-->>Client: afficherConfirmation("✅ Code accepté")
                Note over Client,BD: Étape 3 — Accès aux fonctionnalités

                ATM-->>Client: afficherMenu(["Retrait", "Solde", "Virement", "Quitter"])
                Client->>ATM: choisirAction(action)
                ATM-->>Client: executerAction(action)
                deactivate ATM

            else code incorrect — tentative 1 ou 2
                ATM-->>Client: afficherErreur("❌ Code erroné — tentatives restantes : " + (3 - tentative))
                deactivate ATM

            else code incorrect — 3ème tentative échouée
                ATM-->>Client: avalerCarte("🚫 Trop de tentatives, carte confisquée")
                ATM->>BD: UPDATE cartes SET statut='bloquee' WHERE numero=carteId
                BD-->>ATM: ok
                deactivate ATM
            end

        end

        deactivate ATM
    end
```
