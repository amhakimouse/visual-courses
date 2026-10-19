Un **modificateur d’accès** décide **qui a le droit de voir** une classe, une méthode ou une variable.

### Les 4 niveaux (du plus ouvert au plus fermé)

```
   public      ████████████████████████  tout le monde
   protected   ████████████████          même package + sous-classes
   (package)   ████████████              même package seulement
   private     ████                      la classe elle-même seulement
```

# contrôle d’accès et héritage

Quand une sous-classe **redéfinit** une méthode, elle peut **garder ou élargir**
sa visibilité, jamais la **réduire**.

### L’échelle de visibilité

```
   private  <  (package)  <  protected  <  public
   plus fermé                                plus ouvert

   Redéfinir = on reste au même niveau, ou on monte vers la droite.
```

### Ce qui est permis, selon la superclasse

|Dans la **superclasse**|Dans la **sous-classe**, on peut déclarer|
|---|---|
|`public`|`public` seulement|
|`protected`|`protected` ou `public`|
|_(package)_|_(package)_, `protected` ou `public`|
|`private`|**sans objet** (voir ci-dessous)|

```
   public     ──►  public
   protected  ──►  protected  ou  public
   package    ──►  package    ou  protected  ou  public
```

### Exemple


```java
class Animal {
    public void crier() { }
}

class Chien extends Animal {
    void crier() { }            // ❌ package < public : visibilité réduite
                                // public void crier() { } // ✅
}
```

Erreur de compilation :

```
Cannot reduce the visibility of the inherited method
```

## le modificateur `final`

`final` signifie **« ne peut plus changer »**. Sa portée dépend de ce qu’il modifie.

```
   final  +  classe     →  ne peut pas être SOUS-CLASSÉE
   final  +  méthode    →  ne peut pas être REDÉFINIE
   final  +  variable   →  ne peut pas CHANGER DE VALEUR
```

### Les trois usages

```java
   final class Outil { }                  // personne ne peut faire "extends Outil"

   class A {
       final void f() { }       // les sous-classes ne peuvent pas redéfinir f()
       final int n = 0;                   // n ne changera jamais
   }
```

### Ce que `final` ne peut pas accompagner

```
   final + abstract   ❌   une classe abstraite doit être sous-classée,
                           final l'interdit : contradiction
   final + interface  ❌   même raison
```

### Piège : `final` sur une référence


```java
final Point p = new Point();
p.x = 10;              // ✅ on modifie l'OBJET
p = new Point();       // ❌ on change la RÉFÉRENCE
```

```
   final fige la VARIABLE (la flèche),  pas forcément l'objet pointé.

   p ──────► [ Point  x = 10 ]      l'objet peut changer
   (flèche verrouillée)
```