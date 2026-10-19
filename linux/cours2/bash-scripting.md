# Le shell : interpréteur de commandes


Le **shell** est un programme qui sert d'intermédiaire entre **toi** et le **noyau** (kernel). Il a deux rôles :

- **Interpréteur** : il lit ce que tu tapes et l'exécute.
- **Langage de programmation** : tu peux écrire des scripts (variables, `if`, boucles).

```
┌──────────────┐   commande   ┌──────────────┐   appel système   ┌──────────────┐
│ Utilisateur  │ ───────────► │    SHELL     │ ────────────────► │    NOYAU     │
│  (clavier)   │ ◄─────────── │  (bash)      │ ◄──────────────── │   (Linux)    │
└──────────────┘   résultat   └──────────────┘     résultat      └──────────────┘
```
### Comment ça marche : la boucle infinie

```
        ┌─────────────────────────────────────────┐
        │                                         │
        ▼                                         │
 ┌─────────────┐                                  │
 │ 1. PROMPT   │  affiche  $                      │
 └──────┬──────┘                                  │
        ▼                                         │
 ┌─────────────┐                                  │
 │ 2. LECTURE  │  tu tapes la commande + ENTRÉE   │
 └──────┬──────┘                                  │
        ▼                                         │
 ┌─────────────┐                                  │
 │ 3. ANALYSE  │  découpe en mots                 │
 └──────┬──────┘                                  │
        ▼                                         │
 ┌─────────────┐                                  │
 │ 4. SUBSTIT. │  remplace $var, *, `cmd`...      │
 └──────┬──────┘                                  │
        ▼                                         │
 ┌─────────────┐                                  │
 │ 5. EXÉCUTION│  lance la commande ──────────────┘
 └─────────────┘
```

---
# Flux et redirections
 
Chaque commande est lancée avec **3 canaux** ouverts, numérotés (descripteurs) :

```
                  ┌───────────────┐
 Clavier ──(0)──► │               │ ──(1)──► Écran   (résultat normal)
   stdin          │   COMMANDE    │   stdout
                  │               │ ──(2)──► Écran   (messages d'erreur)
                  └───────────────┘   stderr
```

| N°  | Nom        | Par défaut |
| --- | ---------- | ---------- |
| 0   | **stdin**  | clavier    |
| 1   | **stdout** | écran      |
| 2   | **stderr** | écran      |

**Rediriger** = changer la destination d'un canal vers un fichier.

###  Les opérateurs

|Syntaxe|Effet|Fichier existant|
|---|---|---|
|`cmd > f`|stdout → `f`|**écrasé**|
|`cmd >> f`|stdout → `f`|**ajout à la fin**|
|`cmd 2> f`|stderr → `f`|écrasé|
|`cmd 2>> f`|stderr → `f`|ajout|
|`cmd < f`|stdin ← `f`|lu|
|`cmd > f 2>&1`|stdout **et** stderr → `f`|écrasé|

```
 cmd > f          cmd 2> f             cmd > f 2>&1
 ┌─────┐          ┌─────┐              ┌─────┐
 │ cmd │─1─► f    │ cmd │─1─► écran    │ cmd │─1─► f
 │     │─2─► écran│     │─2─► f        │     │─2─┘ (suit le 1)
 └─────┘          └─────┘              └─────┘
```
### Exemple


```bash
ls /etc /inexistant > sortie.txt   # stdout (liste de /etc) → sortie.txt ; l'erreur sur /inexistant reste à l'écran
ls /etc >> sortie.txt              # ajoute la liste à la fin, sans effacer
ls /inexistant 2> erreur.txt       # le message d'erreur va dans erreur.txt, l'écran reste vide
ls /etc /inexistant > tout.txt 2>&1  # tout (résultat + erreur) dans tout.txt
```

### ⚠️ Point clé 1 : l'ordre compte

`2>&1` signifie : _« envoie stderr là où stdout pointe **à cet instant** »_. Lecture de gauche à droite :

```
 cmd > f 2>&1                      cmd 2>&1 > f
 ───────────────                   ───────────────
 1) stdout ─► f                    1) stderr ─► (stdout = écran)
 2) stderr ─► (stdout = f)         2) stdout ─► f
 ✅ les deux dans f                ❌ stderr reste à l'écran
```

### ⚠️ Point clé 2 : les redirections passent en premier

Le shell traite les redirections **avant** de lancer la commande. Donc :

bash

```bash
commande_inexistante > fich   # fich est créé (ou vidé) même si la commande échoue
> fich                        # équivalent à : crée/vide fich (astuce pour vider un fichier)
> fich commande               # identique à : commande > fich
```

### 🔧 Notation `&n` et fermeture

bash

```bash
cmd > f1 2>&1   # &1 = "le descripteur 1" ; stdout et stderr dans f1
cmd <&-         # ferme stdin
cmd >&-         # ferme stdout
cmd 2>&-        # ferme stderr (les erreurs disparaissent)
```

---
# Script shell et variables

Un **script** = un fichier texte contenant des commandes, exécutées l'une après l'autre.

bash

```bash
#!/bin/bash          # shebang : indique quel interpréteur lance le script
echo "Bonjour"       # première commande du script
date                 # deuxième commande
```

```
 1) Écrire        2) Rendre exécutable     3) Lancer
 ┌──────────┐     ┌──────────────────┐     ┌──────────┐
 │ nano s.sh│ ──► │ chmod a+x s.sh   │ ──► │ ./s.sh   │
 └──────────┘     └──────────────────┘     └──────────┘
```

- `chmod a+x` : `a` = tous (all), `+x` = ajoute le droit d'exécution.
- `./s.sh` : le `./` dit « dans le répertoire courant » (il n'est pas dans le `PATH`).

## les variables

Variables **non typées** (tout est du texte).

bash

```bash
mois=Janvier        # affectation : AUCUN espace autour du =
echo $mois          # $ = lire la valeur → affiche Janvier
unset mois          # supprime la variable
set                 # affiche toutes les variables
env                 # affiche les variables d'environnement (exportées)
```

|❌ Faux|✅ Juste|Pourquoi|
|---|---|---|
|`mois = Janvier`|`mois=Janvier`|avec espaces, le shell croit que `mois` est une commande|

#### Concaténation et accolades

bash

```bash
a=Bon
b=jour
echo $a$b       # Bonjour  (juxtaposition)
echo $b1        # (vide)   le shell cherche la variable "b1", qui n'existe pas
echo ${b}1      # jour1    les accolades délimitent le nom : variable "b" puis "1"
```

## Protection

bash

```bash
readonly pi=3   # variable en lecture seule
pi=4            # ❌ erreur : modification interdite
unset pi        # ❌ erreur : suppression interdite
readonly        # sans argument : liste les variables protégées
```

### la portée (le point le plus important)

Une variable est **locale** au processus qui l'a créée. Un script lancé = un **processus fils**, qui ne voit pas les variables du père, sauf si elles sont **exportées**.

```
 SHELL PÈRE                          PROCESSUS FILS (./f1)
 ┌─────────────────────┐             ┌─────────────────────┐
 │ a=oui   (locale)    │ ── lance ─► │ a = ❌ (invisible)  │
 └─────────────────────┘             └─────────────────────┘

 SHELL PÈRE                          PROCESSUS FILS (./f1)
 ┌─────────────────────┐             ┌─────────────────────┐
 │ export a  (a=oui)   │ ── lance ─► │ a = oui ✅ (hérité) │
 └─────────────────────┘             └─────────────────────┘
```

#### Exemple complet

Fichier `f1` (rendu exécutable avec `chmod a+x f1`) :

bash

```bash
echo "Dans f1 : a = $a"   # affiche la valeur de a vue par le fils
```

Dans le terminal :

bash

```bash
a=oui         # a existe seulement dans le père
./f1          # → Dans f1 : a =          (le fils ne voit rien)
export a      # a entre dans l'environnement
./f1          # → Dans f1 : a = oui      (le fils hérite de a)
```

⚠️ L'export est à **sens unique** : le fils hérite d'une **copie**. Si le fils modifie `a`, le père ne le voit pas.

---

### variables prédéfinies

| Variable           | Contenu                                            |
| ------------------ | -------------------------------------------------- |
| `HOME`             | répertoire de connexion (`cd` seul = `cd $HOME`)   |
| `PATH`             | répertoires où chercher les commandes **externes** |
| `PWD`              | répertoire courant                                 |
| `USER` / `LOGNAME` | nom de connexion                                   |
| `SHELL`            | shell utilisé                                      |
| `PS1`              | prompt principal (défaut `$`)                      |
| `PS2`              | prompt de continuation (`>`)                       |
| `PS3`              | prompt de la commande `select`                     |
| `MAIL`             | boîte aux lettres                                  |
| `MAILCHECK`        | fréquence (en secondes) de vérification de `$MAIL` |
|                    |                                                    |

# Arithmétique

Les variables sont du **texte**. Pour calculer, il faut une commande dédiée.

|Outil|Shell|Syntaxe|
|---|---|---|
|`expr`|Bourne (ancien, commande externe)|`expr 1 + 3`|
|`let`|bash / ksh (interne)|`let a=1+3`|
### **let**
```
 "5" + "9"  ──►  texte "59"  ❌ (pas de calcul)
 let a=5+9  ──►  a = 14      ✅
```

### **expr** (Bourne)

```bash
a=1
a=`expr $a + 3`    # backquotes : exécute expr, récupère son affichage (4) dans a
echo $a            # 4
```


# Paramètres d'un script


Quand tu lances un script avec des **arguments**, le shell les range dans des variables spéciales.

```
 ./demo   un    2    trois
   │      │     │      │
   $0     $1    $2     $3        $# = 3      $* = "un 2 trois"
```

|Variable|Contenu|
|---|---|
|`$0`|nom du script|
|`$1` … `$9`|1er … 9e argument|
|`$#`|**nombre** d'arguments|
|`$*`|**tous** les arguments|
|`$$`|PID du processus courant|
|`$!`|PID du dernier processus lancé en arrière-plan (`&`)|
|`$?`|code de retour de la dernière commande (0 = succès)|
### `shift` : décaler les arguments

`shift` supprime `$1` et fait glisser les autres vers la gauche.

```
 Avant :  $1=a   $2=b   $3=c     $#=3
 shift
 Après :  $1=b   $2=c            $#=2     (a est perdu)
```

# Quotes : `'` `"` `` ` ``

Trois types de guillemets, trois comportements différents.

```
 ┌───────────┬──────────────────────┬───────────────────────┐
 │  '...'    │  "..."               │  `...`  (ou $(...))   │
 │  simple   │  double              │  backquote            │
 ├───────────┼──────────────────────┼───────────────────────┤
 │ TOUT est  │ $variable est        │ le contenu est        │
 │ du texte  │ remplacée, le reste  │ EXÉCUTÉ comme commande│
 │ brut      │ est du texte         │ → on récupère le      │
 │           │                      │   résultat            │
 └───────────┴──────────────────────┴───────────────────────┘
```

### Exemples


```bash
variable="ensa"                       # on crée la variable (SANS $ à gauche du =)

echo 'Mon mot de passe est $variable.'       # simple quote : rien n'est remplacé
# → Mon mot de passe est $variable.

echo "Mon mot de passe est $variable."       # double quote : $variable est remplacée
# → Mon mot de passe est ensa.

echo "Aujourd'hui : `date`"     # backquote dans les doubles : date est exécutée
# → Aujourd'hui : Thu Oct  8 10:00:00 2026
```

### Quelle quote choisir ?

```
 Je veux du texte exact, sans rien remplacer  ──►  '...'
 Je veux du texte + des variables             ──►  "..."
 Je veux le résultat d'une commande           ──►  $(...)
```

# `test` et `[ ]`

###  Concept

`test` évalue une condition et renvoie un **code de retour** (pas d’affichage) :

```
 condition vraie  ──►  code 0   (VRAI)
 condition fausse ──►  code ≠ 0 (FAUX)
```

Deux écritures **identiques** :

bash

```bash
test -x /ensa        # forme test
[ -x /ensa ]         # forme crochets (espaces OBLIGATOIRES après [ et avant ])
echo $?              # affiche 0 si vrai, 1 si faux
```

⚠️ `[` est une vraie commande : `[-x /ensa]` ❌ → « commande introuvable ».

###  Les 3 familles de tests

```
 ┌──────────────┬─────────────────┬──────────────────┐
 │  FICHIERS    │   CHAÎNES       │   ENTIERS        │
 │  -f -d -r    │   = != -z -n    │   -eq -ne -gt... │
 └──────────────┴─────────────────┴──────────────────┘
```

#### A) Fichiers : `-type fichier`

|Option|Vrai si le fichier...|
|---|---|
|`-f`|existe et est un fichier **ordinaire**|
|`-d`|est un **répertoire**|
|`-r` / `-w` / `-x`|est lisible / modifiable / exécutable|
|`-s`|existe et a une taille **> 0**|
|`-c` / `-b` / `-p`|caractère / bloc / tube nommé|
|`-u` / `-g` / `-k`|suid / sgid / sticky|

```bash
[ -d /etc ]          # vrai : /etc est un répertoire
[ -f /etc/passwd ]   # vrai : fichier ordinaire
[ -s vide.txt ]      # faux si le fichier est vide
```

#### B) Chaînes (variables)

|Syntaxe|Vrai si...|
|---|---|
|`-z "$v"`|`v` est de longueur **nulle** (vide)|
|`-n "$v"`|`v` est de longueur **non nulle**|
|`"$a" = "$b"`|chaînes **identiques**|
|`"$a" != "$b"`|chaînes **différentes**|


```bash
rep=q
[ "$rep" = "q" ]     # vrai : rep vaut "q" (guillemets = protection si rep est vide)
[ -z "$vide" ]       # vrai si vide n'est pas définie ou vaut ""
```

#### C) Entiers : `n1 cmp n2`

|Option|Signifie|Option|Signifie|
|---|---|---|---|
|`-eq`|`=`|`-ge`|`>=`|
|`-ne`|`≠`|`-lt`|`<`|
|`-gt`|`>`|`-le`|`<=`|

bash

```bash
[ $# -gt 0 ]         # vrai s'il y a au moins 1 argument
[ 5 -eq 5 ]          # vrai
```

⚠️ **Piège classique** : `=` compare du **texte**, `-eq` compare des **nombres**.

bash

```bash
[ "01" = "1" ]       # FAUX (textes différents)
[ 01 -eq 1 ]         # VRAI (nombres égaux)
```

### 🔗 Combiner les tests

| Opérateur   | Sens                                       |
| ----------- | ------------------------------------------ |
| `-a`        | ET                                         |
| `-o`        | OU                                         |
| `!`         | NON                                        |
| `\( ... \)` | groupement (parenthèses protégées par `\`) |
|             |                                            |

bash

```bash
[ -f fic -a -r fic ]          # fic est un fichier ET lisible
[ $a -lt 0 -o $a -gt 10 ]     # a < 0 OU a > 10
[ ! -d /tmp/x ]               # /tmp/x n'est PAS un répertoire
```

💡 En bash moderne, on écrit aussi : `[ -f fic ] && [ -r fic ]` (ET) et `[ ... ] || [ ... ]` (OU).


## Structures de contrôle

###  Concept

Les structures décident **quoi exécuter** et **combien de fois**. Elles s’appuient sur le **code de retour** (0 = vrai, ≠ 0 = faux).

```
 ┌─────────────┬──────────────────────────────────────┐
 │ if / case   │ CHOISIR  (quelle branche exécuter)   │
 │ for         │ RÉPÉTER  sur une liste de valeurs    │
 │ while/until │ RÉPÉTER  selon une condition         │
 └─────────────┴──────────────────────────────────────┘
```

---

###  A) `if` : choisir

```
          ┌───────────────┐
          │  commande ?   │
          └───┬───────┬───┘
         0 (vrai)   ≠0 (faux)
              ▼       ▼
          then ...   else ...
```


```bash
if [ -f fic1 ]                  # teste si fic1 est un fichier ordinaire
then
  echo "fic1 : fichier"         # exécuté si 1er test vrai
elif [ -d fic1 ]                # sinon, teste si c'est un répertoire
then
  echo "fic1 : répertoire"      # exécuté si 2e test vrai
else
  echo "fic1 : spécial"         # exécuté si aucun test vrai
fi                              # fin du if (if à l'envers)
```

- `elif` et `else` sont **optionnels**.
- La condition peut être **n’importe quelle commande** : `if grep -q root /etc/passwd; then ...`

---

###  B) `for` : parcourir une liste

```
 liste : 1 → 2 → 3 → 4
          │   │   │   │
          ▼   ▼   ▼   ▼
        n=1  n=2 n=3 n=4   (le corps est exécuté 1 fois par valeur)
```


```bash
for n in 1 2 3 4                # n prend successivement 1, 2, 3, 4
do
  cp fic1 /users/rep$n          # 1er tour : cp fic1 /users/rep1, etc.
done                            # fin de la boucle
```

💡 La liste peut venir d’un motif : `for f in *.txt` (tous les `.txt`) ou d’une commande : `for u in $(cat users.txt)`.

---

### 🔁 C) `while` : tant que la condition est vraie

```
        ┌──────────────┐
   ┌──► │ condition ?  │──faux──► SORTIE
   │    └──────┬───────┘
   │         vrai
   │           ▼
   └───── exécute le corps
```

bash

```bash
while [ $# -gt 0 ]              # tant qu'il reste au moins 1 argument
do
  echo "Paramètre = $1"         # affiche le 1er argument courant
  shift                         # le retire : $# diminue → la boucle finira
done
```

⚠️ Sans `shift`, `$#` ne change jamais → **boucle infinie**.

---

### 🔁 D) `until` : jusqu’à ce que (l’inverse de `while`)

```
 while : continue tant que VRAI
 until : continue tant que FAUX  (s'arrête quand la condition devient vraie)
```

bash

```bash
i=1                             # initialisation du compteur
until [ "$i" -eq 10 ]           # répète jusqu'à ce que i vaille 10
do
  echo $i                       # affiche i
  let i=$i+1                    # incrémente i de 1
done                            # affiche 1 à 9
```

⚠️ **Correction du cours** : `[ "$i"=10 ]` (sans espaces) est **toujours vrai** (une seule chaîne non vide) → la boucle ne tournerait jamais. Il faut des espaces et `-eq` pour comparer des nombres.

---

### 🎛️ E) `case` : choisir selon un motif

```
        valeur de $#
             │
     ┌───────┼───────┐
     ▼       ▼       ▼
    0)      1)       *)       ← le 1er motif qui correspond gagne
```

bash

```bash
case $# in                      # compare $# aux motifs ci-dessous
  0) dir=`pwd`;;                # aucun argument : dir = répertoire courant
  1) dir=$1;;                   # 1 argument : dir = cet argument
  *) echo "Erreur de syntaxe"   # tout autre cas (* = joker)
     exit;;                     # quitte le script
esac                            # fin du case (case à l'envers)
```

- `;;` termine chaque branche.
- `*` en dernier = cas **par défaut**.
- Les motifs acceptent des jokers : `[0-9]*)`, `*.txt)`, `a|b)` (OU).


## `alias`, `read`, `eval`, fonctions, `.`

### A) `alias` : un surnom pour une commande

bash

```bash
alias toto='ls -l'    # définit toto = ls -l (quotes simples obligatoires)
toto                  # exécute ls -l
alias                 # liste tous les alias
unalias toto          # supprime l'alias → "toto: not found"
```

```
 toto ──► le shell remplace ──► ls -l ──► exécution
```

⚠️ Un alias vit dans le shell courant : il disparaît à la fermeture (pour le garder, on le met dans `~/.bashrc`).

---

### B) `read` : lire le clavier

bash

```bash
read a b c                    # lit une ligne, la découpe en mots (séparateur : IFS = espace/tab)
read -p "Quel temps ? " x     # -p affiche une invite avant la lecture (bash)
```

```
 Tu tapes :  Ensa  est  une  ecole
              │     │    └────┴── c reçoit TOUT le reste
              a     b            → a=Ensa  b=est  c="une ecole"
```

📌 Règle : s’il y a moins de variables que de mots, la **dernière** récupère le reste.

---

### C) `eval` : double évaluation

Le shell évalue la ligne **une fois**. `eval` force une **2e passe**.

bash

```bash
x=y                  # x contient le NOM d'une autre variable
y=5                  # y contient 5
eval echo \$$x       # accède au contenu du contenu de x
```

```
 Passe 1 (shell) :  \$$x  ──►  $y        (\$ reste littéral, $x devient y)
 Passe 2 (eval)  :  echo $y ──►  5
```

bash

```bash
cmd="ls -l"          # une commande stockée dans une variable
eval $cmd            # eval la relit et l'exécute comme une vraie commande
```

💡 Bash a aussi `${!x}` pour le même effet.

---

### D) Fonctions : des bouts de script nommés

bash

```bash
bonjour()                       # définition : nom suivi de ()
{
  echo "Bonjour $1"             # $1 = 1er paramètre DE LA FONCTION
  echo "Nb args : $#"           # $# = nombre de paramètres de la fonction
}
bonjour Hakim                   # appel : par son nom, comme une commande
# → Bonjour Hakim
# → Nb args : 1
```

```
 bonjour Hakim ──► $1=Hakim, $#=1 ──► exécute le corps ──► retour
```

- Les paramètres s’utilisent comme pour un script : `$1…$9`, `$#`, `$*`.
- `return n` renvoie un code de retour (0 = succès).
- Une fonction doit être **définie avant** son appel.

---

### E) La fonction `.` (point) : exécuter dans le même processus

Un script lancé avec `./s.sh` tourne dans un **fils**. Avec `. s.sh`, il tourne dans le **shell courant**.

```
 ./s.sh                         . s.sh
 ┌────────┐   ┌────────┐        ┌────────────────────┐
 │ PÈRE   │──►│  FILS  │        │ PÈRE exécute lui-  │
 │        │   │ (copie)│        │ même le script     │
 └────────┘   └────────┘        └────────────────────┘
 variables, cd perdus ❌        variables, cd conservés ✅
```

bash

```bash
# fichier fonctions contient : bonjour() { echo "Salut $1"; }
. fonctions          # charge les fonctions dans le shell courant (équivalent : source fonctions)
bonjour Hakim        # → Salut Hakim (disponible car chargée dans CE processus)
```

---

### F) Boucle `while` sur lecture d’un fichier

bash

```bash
while read x                    # lit une ligne dans x ; code ≠ 0 à la fin du fichier → arrêt
do
  echo "Ligne : $x"             # traite la ligne courante
done < fichier                  # tout le bloc lit "fichier" au lieu du clavier
```

```
 fichier ──► ligne 1 ──► x ──► corps
         ──► ligne 2 ──► x ──► corps
         ──► (fin)   ──► read échoue ──► sortie
```

Variante : `cat fichier | while read x` fait la même chose, mais le `while` tourne alors dans un sous-processus (le tube) : les variables modifiées dedans sont **perdues** après `done`. Préfère `done < fichier`.

































