# l'arborescence et les répertoires système

Sous Linux, **tout part d'un seul point : `/` (la racine)**. Il n'y a pas de `C:` ou `D:`.

```
/
├── bin     commandes de base (ls, cp, rm)
├── sbin    commandes réservées à root
├── boot    fichiers de démarrage
├── dev     périphériques (disque, clavier...)
├── etc     configuration du système
├── lib     bibliothèques partagées
├── tmp     fichiers temporaires
├── usr     programmes utilisateurs
├── var     données qui changent (logs, spool)
├── home    dossiers des utilisateurs
│    ├── hakim
│    └── ali
└── root    dossier personnel de l'administrateur
```
---


# le compte utilisateur, `/etc/passwd` et `/etc/shadow`

Un **compte utilisateur** = une **identité** pour le système + un **environnement** de travail.

```
 Compte utilisateur
 ├── identification  →  login, UID, GID           (qui es-tu ?)
 └── environnement   →  homedir, shell            (où et comment tu travailles ?)

 Opérations : création  →  modification  →  destruction
```

### `/etc/passwd` : la fiche d'identité (7 champs séparés par `:`)

```
 kmaster : x : 500 : 500 : kmaster : /home/kmaster : /bin/bash
    1      2    3     4      5            6              7
    │      │    │     │      │            │              └─ shell par défaut
    │      │    │     │      │            └─ homedir (répertoire par défaut)
    │      │    │     │      └─ gecos (identité en clair / commentaire)
    │      │    │     └─ GID (groupe principal)
    │      │    └─ UID (identifiant numérique unique)
    │      └─ mot de passe  →  "x" = stocké dans /etc/shadow
    └─ login
```

### Problème : `/etc/passwd` est lisible par tous

```
 -rw-r--r--  root root  /etc/passwd     ← tout le monde peut LIRE
 -rw-------  root root  /etc/shadow     ← seul root peut lire/écrire
```

```
 AVANT : mot de passe chiffré dans passwd   →  lisible par tous  ✘ risque
 APRÈS : passwd contient "x"                →  le hash est dans shadow  ✔
```

---

# `/etc/group` et la gestion des comptes

### `/etc/group` : lien entre numéro et nom de groupe (4 champs séparés par `:`)

```
 ftpusers : x : 1002 : hakim,ali,sara
     1      2     3         4
     │      │     │         └─ membres (logins séparés par des virgules)
     │      │     └─ GID (numéro du groupe)
     │      └─ champ spécial (mot de passe du groupe, souvent x)
     └─ nom du groupe
```

### Les commandes de gestion

| Action                   | Commande              | Rôle                                          |
| ------------------------ | --------------------- | --------------------------------------------- |
| Créer un utilisateur     | **useradd toto**      | ajoute une ligne dans `passwd` (et `shadow`)  |
| Définir son mot de passe | **passwd toto**       | sans mot de passe, le compte est inutilisable |
| Supprimer un utilisateur | **userdel -r toto**   | `-r` supprime aussi son homedir               |
| Créer un groupe          | **groupadd ftpusers** | ajoute une ligne dans `/etc/group`            |
| Supprimer un groupe      | **groupdel ftpusers** | retire la ligne                               |

```
 useradd toto  ──►  passwd toto  ──►  compte utilisable
   (création)       (mot de passe)

 userdel -r toto  →  supprime : ligne passwd + shadow + /home/toto
 userdel toto     →  supprime le compte mais GARDE /home/toto
```

### Ce que `useradd` doit accomplir (les 9 étapes du cours)

```
 1. choisir UID et GID            6. créer le homedir
 2. choisir le homedir            7. copier les fichiers de config (.profile...)
 3. choisir le login              8. donner le homedir à l'user (chown + chgrp)
 4. choisir le shell              9. initialiser le mot de passe
 5. ajouter dans /etc/group
```

## le compte root, `su` et les fichiers de configuration des shells

### Le compte root

Sa particularité : **UID = 0**. Le système ne regarde pas le nom, il regarde l'UID.

```
 root : x : 0 : 0 : root : /root : /bin/bash
               │
               └─ UID 0 = tous les droits, aucune restriction
```

### 3 règles de sécurité du cours

```
 1. PAS de "." dans le PATH de root
 2. umask = 022
 3. homedir ≠ "/"   (utiliser /root)
```

**Règle 1 : pourquoi pas `.` dans le PATH ?**

```
 PATH contient "." (dossier courant) :

   root est dans /tmp, tape :  ls
   le système cherche d'abord ./ls  →  un faux "ls" piégé laissé par un pirate
   → exécuté avec les droits de root  ✘

 PATH sans "." :  le système ne cherche que dans /bin, /usr/bin...  ✔
 (le cours : "précédence de la commande locale sur la commande système")
```

**Règle 2 : `umask 022`**

Le umask **retire** des droits aux nouveaux fichiers.

```
 fichier créé : 666  (rw-rw-rw-)
 umask        : 022  (----w--w-)    ← droits retirés
 résultat     : 644  (rw-r--r--)    ← les autres peuvent LIRE

 dossier créé : 777 - 022 = 755 (rwxr-xr-x)
```

Sans ça, les fichiers de root seraient illisibles pour les utilisateurs normaux (ex. `/etc/passwd` doit rester lisible).

**Règle 3 : pas `/` comme homedir**

Les fichiers de config de root (`.bashrc`, `.profile`...) polluent la racine `/`. D'où `/root`.

bash

```bash
echo $PATH
umask
```

```
 echo $PATH  →  affiche les dossiers de recherche   →  /usr/local/bin:/usr/bin:/bin
 umask       →  affiche le masque actuel            →  0022
```

---

# La commande `su` : changer d'identité

```
 su  utilisateur2        →  devient utilisateur2, garde SON environnement actuel
 su - utilisateur2       →  devient utilisateur2 AVEC son environnement complet
                (HOME, PATH, fichiers .profile : comme une vraie connexion)
```

```
 hakim$ su - ali
 Password:            ← mot de passe de ali (sauf si on est root)
 ali$ pwd             →  /home/ali       (avec le "-")
 ali$ exit            →  retour à hakim
```

|Commande|Dossier après|Environnement|
|---|---|---|
|`su ali`|reste dans l'ancien|celui de hakim|
|`su - ali`|`/home/ali`|celui de ali|

### Fichiers de configuration des shells

Exécutés **automatiquement** à la connexion pour préparer l'environnement.

```
 Connexion
    │
    ├─► /etc/profile        global : pour TOUS les utilisateurs   (shell sh)
    │
    └─► $HOME/.profile      perso : pour CET utilisateur          (shell sh)
```

|Fichier|Concerne|Rôle|
|---|---|---|
|`/etc/profile`|sh|config globale, exécutée à la connexion|
|`$HOME/.profile`|sh|config perso, exécutée à la connexion|
|`$HOME/.forward`|courrier|redirige le courrier vers une autre adresse|
|`$HOME/.mailrc`|courrier|options, alias|
|`$HOME/.exrc`|vi/ed|configuration des éditeurs|
|`$HOME/.xsession`, `.xinitrc`, `.Xresources`, `.Xdefaults`|multifenêtrage (X)|environnement graphique|

```
 $HOME  =  variable qui contient ton homedir  →  /home/hakim
 fichier commençant par "."  =  fichier caché (visible avec ls -a)
```

---
# cron, les tâches périodiques

**Objectif :** lancer automatiquement une commande à heure fixe (sauvegarde de nuit, mise à jour, etc.), sans être présent.

```
 3 acteurs
 ├── crond     le démon (programme qui tourne en permanence, lancé au boot)
 ├── crontab   le FICHIER qui liste les tâches (un par utilisateur)
 └── crontab   la COMMANDE pour éditer ce fichier
```

```
 boot ──► crond démarre ──► chaque minute, il lit les crontabs
                                   │
                         l'heure correspond ? ──oui──► exécute la commande
```

### Format d'une ligne crontab (6 champs)

```
 15  21  *  *  1   /scripts/sauvegarde.sh
 │   │   │  │  │   └─ commande à exécuter
 │   │   │  │  └─ jour de la semaine : 0 (dimanche) à 6 (samedi)
 │   │   │  └─ mois : 1 à 12
 │   │   └─ jour du mois : 1 à 31
 │   └─ heures : 00 à 23
 └─ minutes : 00 à 59
```

`*` = **toutes les valeurs possibles**.

### Exemples du cours

```
 15 * * * *   /etc.local/cron/scripts/ntpdate
   →  minute 15, n'importe quelle heure, tous les jours  =  toutes les heures à hh:15

 00 21 * * 1  /etc.local/cron/scripts/tartare
   →  21h00 chaque lundi

 00 21 * * 5  /etc.local/cron/scripts/tartare
   →  21h00 chaque vendredi
```

```
 Lecture :  min  heure  jour-mois  mois  jour-semaine
            00   21     *          *     1            →  "à 21:00, un lundi"
```

### Où sont stockés les crontabs ?

```
 Linux    →  /var/spool/cron/
 Solaris  →  /var/spool/cron/crontabs/
 FreeBSD  →  /var/cron/tabs/
```

**Un fichier par utilisateur.** Le crontab de hakim est exécuté avec les droits de hakim.

### Éditer : jamais à la main

Ces fichiers sont du texte, mais on passe **toujours par la commande `crontab`**.

bash

```bash
crontab -e
crontab -l
crontab -l > myfile
vi myfile
crontab myfile
```

```
 crontab -e         →  ouvre ton crontab dans l'éditeur ($EDITOR, sinon vi)
                       et vérifie la syntaxe à l'enregistrement
 crontab -l         →  affiche (list) ton crontab actuel
 crontab -l > myfile→  copie ton crontab dans un fichier
 vi myfile          →  tu modifies la copie
 crontab myfile     →  installe myfile comme nouveau crontab (remplace l'ancien)
```

Option utile : `crontab -r` supprime tout ton crontab (sans confirmation, attention).

### Piège : pas de terminal

```
 Une tâche cron s'exécute SANS terminal  →  pas de stdin, pas de stdout
                                         →  les redirections sont à ta charge
```

```
 30 2 * * *  /scripts/backup.sh > /tmp/backup.log 2>&1
```

```
 >            →  envoie la sortie normale (stdout) dans /tmp/backup.log
 2>&1         →  envoie aussi les erreurs (stderr, n°2) au même endroit que stdout (n°1)
 Sans ça, la sortie est perdue (ou envoyée par mail à l'utilisateur).
```

Aussi : donne toujours le **chemin complet** des commandes (`/usr/bin/...`), car le PATH de cron est réduit.

### Qui a le droit d'utiliser cron ? `cron.allow` / `cron.deny`

| `cron.allow` | `cron.deny` | Utilisateurs autorisés              |
| ------------ | ----------- | ----------------------------------- |
| présent      | présent     | ceux **listés dans cron.allow**     |
| présent      | absent      | ceux **listés dans cron.allow**     |
| absent       | présent     | **tous sauf** ceux dans `cron.deny` |
| absent       | absent      | **root uniquement**                 |

```
 Règle : allow gagne toujours.  Si allow existe, deny est ignoré.
```

---

# les processus 

Un **processus** = un programme **en cours d'exécution**. Le système garde une fiche par processus dans la **table des processus**.

```
 Fiche d'un processus
 ├── PID    numéro unique du processus
 ├── PPID   numéro du processus PARENT (celui qui l'a lancé)
 ├── UID    propriétaire
 ├── GID    groupe
 ├── temps CPU + priorité
 ├── répertoire de travail courant
 └── table des fichiers ouverts
```

### Arbre des processus : PID et PPID

Tout processus vient d'un autre. Le premier est **init** (PID = 1).

```
 démarrage : pseudo-processus (PID 0) ──crée──► init (PID 1, PPID 0)
                                                 │      puis PID 0 disparaît
                                                 └── bash (PID 948, PPID 1)
                                                      └── ps (PID 1169, PPID 948)
```

```
 PPID de ps = 948 = PID de bash  →  bash a lancé ps
```

Sur Ubuntu moderne, `init` est remplacé par **systemd** (toujours PID 1).

### Premier plan et arrière-plan

```
 PREMIER PLAN (foreground)         ARRIÈRE-PLAN (background)
 ───────────────────────           ─────────────────────────
 occupe le terminal                rend le prompt tout de suite
 tu attends la fin                 tu continues à travailler

 $ test.sh                         $ test.sh &
 (prompt bloqué...)                [1] 1165        ← n° de job + PID
                                   $                ← prompt libre
```

- `&` à la fin de la ligne : lance en **arrière-plan**.
- `jobs` : liste les tâches de fond de ce terminal (`jobs -l` ajoute les PID).

### Passer de l'un à l'autre

```
                 Ctrl+Z               bg %1
 PREMIER PLAN ──────────► SUSPENDU ──────────► ARRIÈRE-PLAN (running)
      ▲                                              │
      └──────────────────── fg %1 ───────────────────┘

 Ctrl+C  →  arrête (tue) le processus au premier plan
```

|Action|Commande|Effet|
|---|---|---|
|Suspendre le processus au premier plan|`Ctrl + Z`|statut **Stopped**|
|Reprendre en arrière-plan|`bg %1`|repart en tâche de fond|
|Ramener au premier plan|`fg %1`|reprend le terminal|
|Arrêter|`Ctrl + C`|termine le processus|

`%1` = **numéro de job** (pas le PID).

### Exemple du cours, pas à pas

bash

```bash
test.sh > Sortie.txt
# Ctrl + Z
jobs -l
bg %1
jobs -l
fg %1
# Ctrl + C
```

```
 test.sh > Sortie.txt   →  lance au premier plan, sortie écrite dans Sortie.txt
 Ctrl+Z                 →  [1]+ Stopped      test.sh > Sortie.txt
 jobs -l                →  [1]+ 1162 Stopped   (job 1, PID 1162)
 bg %1                  →  [1]+ test.sh > Sortie.txt &   (repart en fond)
 jobs -l                →  [1]+ 1162 Running
 fg %1                  →  revient au premier plan
 Ctrl+C                 →  arrêt définitif
```

### Suspendre un processus déjà en arrière-plan

`Ctrl+Z` agit sur le premier plan seulement. Pour un job de fond, on envoie un **signal** avec `kill`.

bash

```bash
test.sh > Sortie.txt &
jobs -l
kill -STOP %1
jobs -l
kill -CONT %1
jobs -l
```

```
 test.sh ... &   →  [1] 1165          lancé en fond
 kill -STOP %1   →  met en pause       →  "Signal d'arrêt" (Stopped)
 kill -CONT %1   →  reprend (continue) →  Running
```

`kill` n'est pas qu'un "tueur" : il **envoie un signal** (on le détaille au concept 7).

### Afficher les processus : `ps`

bash

```bash
ps -l
```

```
 F S  UID  PID PPID C PRI NI ADDR  SZ WCHAN  TTY    TIME     CMD
 0 S  500  948  672 0  70  0  -   641 wait4  pts/2  00:00:00 bash
 0 R  500 1169  948 0  79  0  -   772 -      pts/2  00:00:00 ps
```

| Colonne                | Sens                                          |
| ---------------------- | --------------------------------------------- |
| `S`                    | état : `S` endormi, `R` en cours (running)    |
| `UID` / `PID` / `PPID` | propriétaire / n° / n° du parent              |
| `PRI` / `NI`           | priorité / valeur "nice"                      |
| `SZ`                   | taille en mémoire                             |
| `WCHAN`                | canal d'attente (avec quoi il se synchronise) |
| `TTY`                  | terminal associé                              |
| `TIME`                 | temps CPU consommé                            |
| `CMD`                  | commande                                      |

`ps -l` = format **long** (l = long). Autres usages courants : `ps aux` (tous les processus du système), `ps -ef` (avec PPID).

----
# `kill` et les signaux

Un **signal** = un message envoyé à un processus pour lui demander (ou lui imposer) quelque chose.

```
 kill [-signal] PID

 toi ──── kill -15 1234 ────► processus 1234
          (envoie le signal 15)
```

`kill` **n'est pas qu'un tueur** : c'est un **envoyeur de signaux**. Sans option, il envoie le signal 15.

### Lister les signaux

bash

```bash
kill -l
```

```
 kill -l  →  1) SIGHUP  2) SIGINT  3) SIGQUIT ... 9) SIGKILL ... 15) SIGTERM ...
```

### Les 4 signaux principaux du cours

|N°|Nom|Effet|Peut être ignoré ?|
|---|---|---|---|
|1|`SIGHUP`|demande aux **démons** de **relire leur configuration**|oui|
|2|`SIGINT`|interruption (= `Ctrl + C`)|oui|
|9|`SIGKILL`|tue **sans demander son avis**|**non**|
|15|`SIGTERM`|demande **poliment** de se terminer proprement (**défaut**)|oui|

```
 SIGTERM (15)  "Peux-tu t'arrêter, s'il te plaît ?"
                → le processus nettoie (ferme fichiers, sauvegarde) puis quitte  ✔

 SIGKILL (9)   arrêt immédiat imposé par le noyau
                → aucun nettoyage : fichiers corrompus possibles  ✘
```

```
 Bonne pratique :   d'abord kill PID  (15)
                    si le processus ne répond pas  →  kill -9 PID
```

### SIGHUP : recharger sans redémarrer

```
 démon (ex. syslogd) en marche
        │
   kill -1 PID  ──►  relit sa config (/etc/syslog.conf)  ──►  reste actif
```

|Démon|Fichier relu|
|---|---|
|`syslogd`|`/etc/syslog.conf`|
|`inetd`|`/etc/inetd.conf`|
|`sendmail`|`/etc/sendmail.cf`|
|`named`|`/etc/named.boot` (`.conf`)|

Avantage : pas de coupure de service pour appliquer une nouvelle configuration.

### Exemple complet à tester

bash

```bash
sleep 300 &
jobs -l
kill %1
jobs -l
```

```
 sleep 300 &   →  [1] 4521        pause de 300 s, en arrière-plan
 jobs -l       →  [1]+ 4521 Running  sleep 300 &
 kill %1       →  envoie SIGTERM au job 1
 jobs -l       →  [1]+ 4521 Terminated  sleep 300
```

Avec un PID au lieu du job :

bash

```bash
sleep 300 &
ps -l
kill 4521
```

```
 ps -l      →  repère le PID de sleep dans la colonne PID
 kill 4521  →  SIGTERM envoyé au PID 4521
```

### Syntaxes équivalentes

```
 kill -9 1234
 kill -SIGKILL 1234        →  même chose
 kill -KILL 1234           →  même chose

 kill %1                   →  cible un JOB (numéro de job)
 kill 1234                 →  cible un PID
```