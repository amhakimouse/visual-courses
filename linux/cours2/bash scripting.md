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
variable="ensa"                              # on crée la variable (SANS $ à gauche du =)

echo 'Mon mot de passe est $variable.'       # simple quote : rien n'est remplacé
# → Mon mot de passe est $variable.

echo "Mon mot de passe est $variable."       # double quote : $variable est remplacée
# → Mon mot de passe est ensa.

echo "Aujourd'hui : `date`"                  # backquote dans les doubles : date est exécutée
# → Aujourd'hui : Thu Oct  8 10:00:00 2026
```










































