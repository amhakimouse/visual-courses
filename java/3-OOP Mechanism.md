# `static` (variable d’instance vs variable de classe)

### En une phrase

Une variable **d’instance** appartient à **chaque objet**. Une variable **static** appartient à **la classe** et elle est **partagée** par tous les objets.

```
                    CLASSE Voiture
              ┌─────────────────────────┐
              │  static nbrRoues = 4    │  ◄── UNE seule copie (partagée)
              │  static vitesseMax = 300│
              └────────────┬────────────┘
                           │ lue par tous
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   ┌───────────┐     ┌───────────┐     ┌───────────┐
   │ v1        │     │ v2        │     │ v3        │
   │ couleur:  │     │ couleur:  │     │ couleur:  │
   │ "rouge"   │     │ "bleu"    │     │ "noir"    │
   └───────────┘     └───────────┘     └───────────┘
     sa copie          sa copie          sa copie
```
### Le code du cours

```java
class Voiture {
    String couleur;               // instance : une copie par objet
    String marque;                // instance
    int nbrPortes;                // instance
    static int nbrRoues;          // classe : partagée par les Objets
    static int vitesseMax = 300;  // classe : partagée, avec valeur initiale
    Moteur motor;                 // instance
}
```

|                   | Variable d’instance                       | Variable de classe                 |
| ----------------- | ----------------------------------------- | ---------------------------------- |
| Mot-clé           | aucun                                     | `static`                           |
| Déclarée          | dans la classe, **hors** de toute méthode | pareil, + `static`                 |
| Copies en mémoire | **une par objet**                         | **une seule**                      |
| Changer la valeur | n’affecte que cet objet                   | **affecte tous les objets**        |
| Accès             | `v1.couleur`                              | `Voiture.nbrRoues` (via la classe) |

# méthode d’instance vs méthode de classe (`static`)

Une méthode **d’instance** agit sur **un objet précis**. Une méthode **static** décrit un comportement de **la classe entière**, sans objet.

```
   MÉTHODE D'INSTANCE                    MÉTHODE STATIC
   ──────────────────                    ──────────────
   v1.surface()                          Character.isUpperCase('d')
     │                                      │
     └─ besoin d'un OBJET (v1)              └─ besoin de la CLASSE seulement
     └─ peut lire SES attributs             └─ aucun objet "courant"
     └─ this = v1                           └─ this n'existe PAS
```

### La structure d’une méthode (4 parties)

```
   TypeRetourné  nomMéthode ( type1 arg1, type2 arg2 )  {  corps  }
        # ①             ②              ③                      ④
```

# `new` et les constructeurs

`new` **fabrique** un objet. Le **constructeur** est la méthode spéciale que la JVM appelle automatiquement pour l’**initialiser**.

```java
Voiture v = new Voiture("rouge");
//          └─ opérateur new + appel d'un constructeur
```

### Les étapes de `new`

```
   new Voiture("rouge")
        │
        ▼
   ① Allouer la mémoire        [ ??? ]
        │
        ▼
   ② Valeurs par défaut         couleur = null, nbrPortes = 0
        │                    (0 nombres | false boolean | null objets | '\0' char)
        ▼
   ③ Blocs d'initialisation     { ... }
        │
        ▼
   ④ Constructeur appelé        Voiture(String c) { ... }
        │
        ▼
   objet prêt, la variable v reçoit sa référence
```

### Règle clé : la 1re instruction

Un constructeur doit commencer par appeler un autre constructeur :

```
   this(arg1, ..., argN)    → un autre constructeur de la MÊME classe
   super(arg1, ..., argN)   → un constructeur de la SUPER-classe
```

```
   Object ──► Employe ──► Developpeur
     ①           ②            ③        ordre d'exécution
```

Les constructeurs parents s’exécutent en premier, ce qui garantit que les variables héritées sont initialisées avant celles de la sous-classe.

### Surcharge de constructeurs + `this(...)`

```java
class Voiture {
    String couleur;
    int nbrPortes;

    Voiture(String couleur, int nbrPortes) {
        this.couleur = couleur;
        this.nbrPortes = nbrPortes;
    }

    Voiture(String couleur) {
        this(couleur, 4);          // réutilise l'autre constructeur
    }
}

new Voiture("rouge", 2);   // 1er constructeur
new Voiture("bleu");       // 2e constructeur (nbrPortes = 4)
```


# passage d’arguments par valeur

### Cas 1 : un type primitif

java

```java
static void m(int n) { n = n + 1; }

int a = 5;
m(a);
// a vaut toujours 5
```

```
   a = 5 ──copie──► n = 5 ──n+1──► n = 6   (la copie change)
   a = 5                                    (l'original ne bouge pas)
```

### Cas 2 : un objet

Quand on passe un objet, ce n’est **pas l’objet** qui est copié, mais la **référence** (l’adresse) vers lui.

Les deux variables pointent **le même objet**. On peut donc **modifier l’objet** via la copie :

```java
static void m(Point p) { p.x++; }

Point p = new Point();   // x = 1
m(p);
// p.x vaut maintenant 2  (l'objet a été modifié)
```

# les tableaux

Un **tableau** stocke plusieurs valeurs **du même type** sous un seul nom. C’est un **objet** : la variable ne contient qu’une **référence** vers lui.

```
   int[] tab = {10, 20, 30}; or int tab[];

   tab ──────► ┌────┬────┬────┐
  (référence)  │ 10 │ 20 │ 30 │      cases numérotées de 0 à 2
               └────┴────┴────┘
                [0]  [1]  [2]
```

### Les 3 étapes de création

```
   ① Déclarer        ② Réserver la mémoire      ③ Remplir
   Point[] pt;       pt = new Point[10];        for (int i=0; i<10; i++)
                                                    pt[i] = new Point();
```

### Le code des slides (classe `Tableaux`)

java

```java
int[] tab = {1, 2, 3};                 // déclaration + remplissage d'un coup
int[] matrice[] = {{1}, {2}, {3}};     // tableau de tableaux (matrice)
int[][] matrice2 = {{1}, {2}, {3}};
int matrice3[][] = {{1}, {2}, {3}};

// tab = {1, 2, 3};                    // ❌ erreur de compilation
tab = new int[] {1, 2, 3};             // ✅ avec new

Arrays.sort(tab);                      // trie
int pos = Arrays.binarySearch(tab, 2); // cherche 2 → renvoie la position (1)
System.arraycopy(new int[]{1,2,3}, 0, new int[3], 0, 3);   // copie
```

# transtypage entre types primitifs

Le **transtypage** (cast) convertit une valeur d’un type vers un autre. Aller vers un type **plus large** est automatique. Aller vers un type **plus étroit** doit être demandé, et peut **faire perdre de l’information**.

### Élargissement (implicite) : sans risque

```
   byte ──► short ──► int ──► long ──► float ──► double
                       ▲
                      char
```

On peut convertir **sans rien écrire** un type plus petit vers un type plus large :

```java
byte b = 89;
int  i = b;        // OK, automatique
long l = i;        // OK
```

# transtypage entre références

Pour les objets, on ne change pas la valeur, on change **la façon de voir**l’objet. Monter dans la hiérarchie est automatique, descendre demande un cast et peut échouer.
 
```
             Animal            ◄── plus LARGE (type général)
                ▲
                │  extends
              Chien            ◄── plus PRÉCIS (type spécifique)
```

### Élargissement (implicite) : `SuperClasse su = new SousClasse();`

java

```java
Animal a = new Chien();     // OK, automatique : un Chien EST un Animal
```

Deux notions à distinguer :

```
   Animal  a  =  new Chien();
   └──┬──┘        └──┬──┘
   type STATIQUE    type DYNAMIQUE
   (déclaré)        (réel, en mémoire)
```

### Rétrécissement (explicite) : `(A) b`

Descendre dans la hiérarchie demande un cast, et deux vérifications se déclenchent.

```
   ① COMPILATION                         ② EXÉCUTION
   Le cast est-il plausible ?            L'objet est-il vraiment de ce type ?
        │                                      │
        ▼                                      ▼
   erreur de compilation                 ClassCastException
```

