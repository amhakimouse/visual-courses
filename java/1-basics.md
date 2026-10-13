
Java a **8 types primitifs**, avec des **tailles fixes** sur toutes les plateformes. En C++, `int` ou `long` dépendent du compilateur et de l’OS.

# Types


|Type|Bits|Plage|Wrapper|
|---|---|---|---|
|`byte`|8|-128 → 127|`Byte`|
|`short`|16|-32 768 → 32 767|`Short`|
|`char`|16|`\u0000` → `\uFFFF` (0 → 65535)|`Character`|
|`int`|32|≈ ±2,1 × 10⁹|`Integer`|
|`long`|64|≈ ±9,2 × 10¹⁸|`Long`|
|`float`|32|≈ ±3,4 × 10³⁸|`Float`|
|`double`|64|≈ ±1,8 × 10³⁰⁸|`Double`|
|`boolean`|n/a|`true` / `false`|`Boolean`|

### Initialisation (littéraux)


```java
int x = 35;                 // littéral entier = int par défaut
double d = 3.56;            // littéral décimal = double par défaut
byte index = 109;           // OK : 109 tient dans [-128,127], conversion auto pour un littéral constant
long mils = 1234567890L;    // suffixe L : sans lui, le littéral est un int (erreur si trop grand)
float f = 35.09f;           // suffixe f OBLIGATOIRE : sinon 35.09 est un double -> erreur de compilation
boolean flag = true;        // uniquement true ou false
char lettre = 'A';          // apostrophes simples = char ; guillemets doubles = String
char jim = '\u062C';        // séquence Unicode en hexadécimal (ici la lettre arabe ج)
char tm = '\u2122';         // le symbole ™
```

# Overflow / Underflow
Quand un résultat **dépasse la capacité du type**, Java **ne lève aucune erreur** : il continue silencieusement avec une valeur fausse.

```
n = 2 000 000 000
n * n = 4 000 000 000 000 000 000   (a besoin de 64 bits)

64 bits : 00110111 10000010 11011010 11001110 | 10011101 10010000 00000000 00000000
          └──── poids fort : JETÉS ───────────┘ └──── poids faible : GARDÉS ────────┘

32 bits gardés : 10011101 10010000 00000000 00000000
                 ↑
                 bit de signe = 1  →  nombre NÉGATIF  →  -1 651 507 200
```

### 2. Le cercle des entiers

```
              0
        -1 ◀──┼──▶ 1
   -2 ...     │     ... 2
      \       │       /
  -2³¹ ───────┼─────── 2³¹-1     ← MAX_VALUE
              │
   MAX_VALUE + 1  ──▶  MIN_VALUE   (on retombe de l'autre côté)
```


```java
int max = Integer.MAX_VALUE;   // constante : 2147483647
int boom = max + 1;            // dépasse la plage de 1
System.out.println(boom);      // -2147483648 = Integer.MIN_VALUE

byte b = 127;                  // max d'un byte
b++;                           // 127 + 1 → -128
System.out.println(b);         // -128
```

### 3. Décimaux (`float`, `double`) : pas de boucle

| Situation                        | Résultat   | Exemple                 |
| -------------------------------- | ---------- | ----------------------- |
| **Overflow** (trop grand)        | `Infinity` | `Double.MAX_VALUE * 10` |
| **Underflow** (trop proche de 0) | `0.0`      | `Double.MIN_VALUE / 10` |

# Types références et `String`

```
Primitif :  int x = 5;                [ x | 5 ]            ← la valeur est dans la variable
Référence : String s = "Hi";          [ s | ───▶ objet "Hi" ]  ← la variable pointe vers l'objet
```


```java
String a = new String("Hi");   // crée un nouvel objet dans le tas
String b = new String("Hi");   // un autre objet, même contenu
a == b;                        // false : == compare les ADRESSES
a.equals(b);                   // true  : equals compare le CONTENU (toujours l'utiliser pour String)
a.intern() == b.intern();      // true  : intern() renvoie la version unique du pool de chaînes

String s = "Bonjour";          // String est IMMUABLE : aucune méthode ne la modifie
s.length();                    // 7
s.charAt(0);                   // 'B'
s.substring(0, 3);             // "Bon"  (début inclus, fin EXCLUE)
s.split("j");                  // ["Bon", "our"]  (retourne un nouveau tableau)
s.matches("[A-Z].*");          // true  (regex ; le nom réel est matches, pas match)
s.toUpperCase();               // retourne une NOUVELLE chaîne, s reste inchangée
```


## Opérateurs

| `&&` **\|\|**                          | `&` **\|**                           |
| -------------------------------------- | ------------------------------------ |
| Arrêtent dès que le résultat est connu | Évaluent **toujours** les deux côtés |

```java
if (p != null && p.length() > 0) { }   // sûr : si p est null, la 2e partie n'est jamais
```

### Complément à deux

```
Positif : binaire normal           5  = 0000 0101
Négatif : inverser les bits + 1   -5  = 1111 1010  (+1) → 1111 1011

Plage sur n bits : -2^(n-1) → 2^(n-1) - 1     (byte : -128 → 127)
Le bit de poids fort = bit de signe (1 = négatif)
```

### 10. Instructions de contrôle de flot

| Instruction                      | À retenir (spécifique à Java)                                                                                                                                                                        |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `if / else`                      | La condition est obligatoirement un `boolean` entre parenthèses. if (x = 5) est une erreur de compilation. Le `else` se rattache au **if** le plus proche (_dangling else_) : utilise des accolades. |
| `switch`                         | Accepte `char`, `byte`, `short`, `int`, `String`, `enum`. Sans `break`, l’exécution tombe dans le case suivant. `default` est facultatif.                                                            |
| `for`                            | `for (init; condition; mise_à_jour)`. Variante _for-each_ : `for (String s : tableau)`.                                                                                                              |
| `while`                          | Teste **avant** : peut ne jamais s’exécuter. `while (c);` avec `;` est une boucle vide (bug silencieux).                                                                                             |
| `do-while`                       | Teste **après** : s’exécute **au moins une fois**. Le `;` final est obligatoire.                                                                                                                     |
| `break`                          | Quitte la boucle ou le `switch`.                                                                                                                                                                     |
| `continue`                       | Saute à l’itération suivante.                                                                                                                                                                        |
| `break label` / `continue label` | Pas de `goto` en Java : le label permet de sortir d’une **boucle externe**.                                                                                                                          |
| `try-catch-finally`              | `catch` attrape l’exception ; `finally` s’exécute **toujours** (erreur ou non).                                                                                                                      |
| `return`                         | Termine la méthode ; `return valeur;` doit correspondre au type déclaré, `return;` pour `void`.                                                                                                      |


```java
externe:                                  // label placé devant la boucle
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) continue;             // saute seulement l'itération courante de la boucle interne
        if (i == 1) break externe;        // quitte les DEUX boucles d'un coup
        System.out.println(i + "," + j);  // affiche 0,0 puis 0,2
    }
}

try {
    int r = 10 / 0;                       // lève ArithmeticException
} catch (ArithmeticException e) {         // e n'existe que dans ce bloc
    System.out.println("Erreur : " + e.getMessage());
} finally {
    System.out.println("Toujours exécuté");  // fermeture de ressources, nettoyage...
}
```

# Méthodes en Java

### Fonction vs méthode

**Java n’a pas de fonctions.** Il n’a que des **méthodes** : une fonction qui appartient à une classe (ou à un objet).

### Anatomie

```java
public static int addition(int a, int b) {  // [accès] [static] type_retour nom(paramètres)
    int somme = a + b;                  // corps : déclaration + expression
    return somme;                     // renvoie une valeur du type annoncé (int)
}
```
### Les types de méthodes

#### 1. Selon le retour


```java
void afficher(String msg) {          // void : ne retourne rien
    System.out.println(msg);         // effet de bord seulement
    return;                          // facultatif en void
}

int carre(int x) {                   // retourne une valeur : return OBLIGATOIRE sur tous les chemins
    return x * x;                    // le type renvoyé doit correspondre à int
}
```

#### 2. Selon l’appartenance : ==🔴`static` vs `instance`==

```
         ┌──────────── Classe Compte ────────────┐
         │  static  : UNE seule copie, partagée  │
         │  instance: une copie PAR objet        │
         └───────────────────────────────────────┘
              ▲                      ▲
        Compte.methodeStatic()   c1.methodeInstance()
        (pas d'objet requis)     (objet requis : accède à SES données)
```

```java
public class Compte {
    private double solde;                     // attribut d'instance : propre à chaque objet
    static int nbComptes = 0;                 // attribut static : commun à tous

    void deposer(double m) {                  // méthode d'INSTANCE
        solde += m;                           // accède à l'attribut de CET objet
    }

    static int total() {                      // méthode STATIC
        return nbComptes;                     // ne voit PAS solde : aucun objet associé
    }
}

// Utilisation
Compte c = new Compte();     // création d'un objet (new)
c.deposer(100);              // instance : appelée sur l'objet c
Compte.total();              // static : appelée sur la classe
```


### Concepts propres aux méthodes

#### Surcharge (_overloading_) : même nom, paramètres différents

```java
int    somme(int a, int b)         { return a + b; }       // version 1
double somme(double a, double b)   { return a + b; }       // version 2 : types différents
int    somme(int a, int b, int c)  { return a + b + c; }   // version 3 : nombre différent
// Le compilateur choisit selon les arguments. Changer seulement le type de retour ne suffit PAS.
```

#### Arguments variables (_varargs_)

```java
int somme(int... nombres) {          // ... : 0, 1 ou N entiers ; nombres est un int[] dans le corps
    int s = 0;
    for (int n : nombres) s += n;    // for-each sur le tableau
    return s;
}
somme(1, 2, 3, 4);                   // 10
```

## `String` : littéral vs `new`

### Mémoire : où vit chaque objet ?

L’affichage est identique (`TAT` ×4), mais les **objets** diffèrent. Voici comment le voir :

```java
String s1 = "TAT";
String s2 = "TAT";
String s3 = new String("TAT");
String s4 = new String("TAT");

System.out.println(s1 == s2);        // true  : même objet du pool (même adresse)
System.out.println(s1 == s3);        // false : s3 est un objet distinct
System.out.println(s3 == s4);        // false : deux objets distincts
System.out.println(s1.equals(s3));   // true  : equals compare le CONTENU
System.out.println(s1 == s3.intern());// true : intern() renvoie la version du pool
```

```
            PILE (variables)             TAS (objets)
                                   ┌──────────────────────────┐
  s1 ──────────────────────────────┼──▶ ┌───────┐             │
  s2 ──────────────────────────────┼──▶ │ "TAT" │  ◀── POOL   │
                                   │    └───────┘  (1 seul)   │
  s3 ──────────────────────────────┼──▶ ┌───────┐  hors pool  │
                                   │    │ "TAT" │             │
  s4 ──────────────────────────────┼──▶ ┌───────┐             │
                                   │    │ "TAT" │  (autre)    │
                                   └──────────────────────────┘
```


# `StringBuilder` et `StringBuffer`

`String` est **immuable** : chaque modification crée un nouvel objet. `StringBuilder` et `StringBuffer` sont des **chaînes modifiables** : on change le **même objet** sans le recopier.

```
String         "abc" ──+"d"──▶ NOUVEL objet "abcd"      (l'ancien reste en mémoire)
StringBuilder  [a|b|c|_|_|...] ──append("d")──▶ [a|b|c|d|_|...]   (même objet, tampon modifié)
```

```
Thread 1 ──┐                         Thread 1 ──┐
           ├──▶ StringBuilder ❌               ├──▶ StringBuffer ✅
Thread 2 ──┘   (résultat imprévisible)  Thread 2 ──┘   (un thread à la fois)
```


































