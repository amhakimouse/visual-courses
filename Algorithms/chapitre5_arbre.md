Chapitre 5 : Structures de données hiérarchiques
2
Plan
Introduction
Arbre
Arbre binaire (AB)
Représentation SDD d'un AB
Algorithmes de parcours d'un AB
Algorithmes sur un AB
Arbres binaires de recherche (ABR) Équilibrage et arbre AVL
3
Introduction
Naturels
Organigramme d'une entreprise
Résultat d'un tournoi
...
finale
vainqueur
demi-finales
Eq1
Eq5
Eq3
Eq7 quarts de finales
Eq2
Eq6
Eq4
Eq8
4
Introduction
Informatiques
Système de fichiers
Langages et compilation
(Arbre de dérivation, Arbre d'analyse)
Traitements récursifs
...
mnt bin boot dev etc home lib media
bash cat grub abi cpu
max elsa
images
documents
grub.cfg
photos_vac ski fiche.ods
photo_1.jpg
gdbd_3.jpg
usb0
boulot
rapport.odt
système de fichiers de type UNIX
5
Utilisation d'un arbre
Structure fondamentale de l'informatique
☐ Définition et traitement naturellement récursifs
☐ En précisant une relation d'ordre sur les éléments
☐ Arbre de recherche (Ordre horizontal)
☐ Structure de tas (Ordre vertical)
☐ En précisant une condition d'équilibre
Arbre auto-équilibrés (AVL)
...
6
Définition
Un arbre est une structure de données organisées de façon hiérarchique, à partir d'un nœud distingué appelé racine. Un élément quelconque peut avoir plusieurs successeurs, mais un seul prédécesseur. Seul le premier élément n'a pas de
prédécesseur.
noeuds
arêtes
7
Définition (SDD)
Les arbres sont enracinés. Une fois la racine définit tous les nœuds admettent un niveau.
Les arbres ont des nœuds internes et des feuilles (nœuds
externes).Chaque nœud a un parent (à l'exception de la racine) et admet zéro ou plusieurs fils.
racine
niveau 0
niveau 1
nœuds internes
niveau 2
niveau 3
parent et
fils
feuilles
8
Définition (SDD)
Ensemble hiérarchisé de nœuds (Containers d'élément)
Un nœud racine unique ou inexistant (arbre vide)
Chaque nœud non racine possède un unique parent
Chaque nœud peut posséder deux enfants (fils gauche et fils
droit)
Définition
Un arbre est un ensemble de nœuds, reliés par des Arêtes. Entre
deux nœuds il existe toujours un seul chemin.
9
Qualification des nœuds
☐ Par transitivité de la relation parent-enfant
Ancêtre ou ascendant vs. descendant
Propriété : la racine est l'ancêtre de tous les nœuds
☐ Nœuds frères : qui ont le même parent Feuille ou nœud externe : qui n'a pas d'enfant Nœud interne : qui au moins un enfants
10
Branches, couches
☐ Branche (a, b) où b descend de a
☐ Ensemble : a, b et ancêtres de b qui descendent de a
☐ Branche extérieure gauche vs. droite
☐
☐ Branche (racine, feuille la plus à gauche vs. droite)
Couche de profondeur n
☐ Ensemble des nœuds situés à la profondeur n
11
Mesures
☐ Distance entre deux nœuds..
☐
☐
☐ qui forment une branche (a, b)
..
☐ Nombre d'éléments de la branche moins un
☐
Profondeur d'un nœud
Sa distance à la racine
☐ Note: la racine est donc de profondeur O Hauteur d'un arbre
☐ Profondeur de la feuille la plus profonde
12
Vocabulaire
branche: chemin à la racine
ancetre
profondeur=2
descendant
racine
niveaux
frère
hauteur=5
13
Sous-arbres, définition récursive
☐
☐
Pour tout nœud
☐ Le fils gauche est la racine du sous-arbre gauche
☐ Le fils droit est la racine du sous-arbre droit
Définition alternative (récursive) d'un arbre
☐ Un arbre est un triplet (a, G, D) composé
D'un nœud racine a
D'un sous-arbre gauche G
D'un sous-arbre droit D
14
Arbres spéciaux
Arbre vide
☐ N'a aucun nœud = est sans racine
Arbre entier
Dont tous les nœuds sont soit interne, soit feuille
Arbre complet
☐ Arbre entier
Π Pas de feuilles dont les profondeurs diffèrent > 1 Arbre parfait
☐ Arbre entier
☐ Pas de feuilles dont les profondeurs diffèrent
15
Représentation SDD d'un Arbre Binaire
Définition d'arbre binaire
Arbre Binaire: un arbre où chaque nœud admet au plus 2 fils.
Chaque noeud a au plus 2 fils: le fils gauche et le fils droit
sous-arbre gauche
fils gauche
noeud
sous-arbre droit (sa racine est
fils droit
17
Définition d'arbre binaire
☐ Reproduction de la définition récursive
☐ Possibilité d'implémentation statique (cf. listes, piles, files)
☐
Représentation simplement chaînée
☐ La plus naturelle
☐ La plus simple à mettre en œuvre
Un arbre binaire de hauteur h contient au plus $2^{h}-1$ noeuds
(hauteur = nombre de niveaux)
18
Définition d'arbre binaire
Arbre Binaire complet : est un arbre binaire dont chaque sommet interne a exactement deux fils.
les feuilles sont toutes situées dans les deux derniers niveaux. Les feuilles du dernier niveau sont toutes à gauche.
10
14
16
8
12
15
18
7
9
11 13
19
Définition d'arbre binaire
Un arbre binaire complet peut être représenté par un tableau A
avec un accès en $O(1)$ à chaque nœud:
Mémoriser les nœuds séquentiellement de la racine aux feuilles et de gauche vers la droite.
Fils gauche de $A[i]$ est en $A[2i]$
Fils droit de $A[i]$ est en $A[2i+1]$
1 14
2
3
(10
16
4
56
7
$A[i/2]$
8
12 15
18
9 10
8
7
9
1
2
3 4 5 6
7
8 9 10
11
1113
tab A:
14 10
16 8
12 15 18
79
11 13
Parent de $A[i]$ est en
20
Définition d'arbre binaire
racine
1
2
nombre de noeuds
Arbre binaire complet :
à la profondeur p: $2^{p}$ noeuds
nombre total de noeuds : $\sum_{i=0}^{h-1}2^{i}=2^{h}-1$
4
8
16
21
Définition d'un nœud d'arbre
Structure nœud comportant deux champs 1. un élément e
2. l'adresse mémoire sag du sous-arbre gauche 3. l'adresse mémoire sad du sous-arbre droit
A
sag
sad
22
Assembler un arbre
Notez l'identité maillon LDC et nœud d'AB
Les deux pointeurs changent de nom (convention)
Ce qui change fondamentalement
☐ La manière d'assembler les instances de ces maillons
☐ Graphe acyclique
A
NON!
on s'interdit de former des cycles
B
A
NON!
23
Assembler un arbre
A
B
C
+
OUI!
A
24
Définition d'un nœud d'AB
Algorithme
type...: T
: Définition de la structure d'un noeud d'arbre binaire (AB)
type structure noeud
fin
info: T
sag, sad: adresse noeud
type adresse noeud : arbre
typedef int Element;
typedef struct node {
Element elem;
struct node *left;
struct node *right; }Node;
typedef Node *BTree;
25
Implémentation d'AB
12
racine.filsG
1
1
7
91
91
67
82
14
11
14
racine
12
67
11
7
82
racine.filsD.filsD
26
Quelques fonctions de base
Algorithme
: EstArbre Vide(a: arbre): booléen
Donnée
Résultat
: L'arbre a à évaluer : Un booléen
début
si $a=$ nul alors retourner vrai
sinon retourner faux
fin
27
Quelques fonctions de base
Algorithme
: Créer Noeud(e: T): arbre
Variable locale : L'arbre a créé et initialisé (arbre singleton) Variable locale : L'élément e à stocker dans la racine de a
Résultat
début
: α
a réserver noeud
$a\rightarrow info\leftarrow e$
$a\rightarrow sag\leftarrow\emptyset$
fin
$a\rightarrow sad\leftarrow\emptyset$
retourner a
28
Algorithmes de parcours
d'un Arbre Binaire
Parcourir les nœuds d'un arbre
☐ Problème
☐ Comment parcourir un AB, i.e.
☐ Comment visiter chaque nœud une fois et une seule?
☐ Deux grand types de parcours
☐ En largeur
☐
☐ Niveau par niveau
Naturellement itératif
En profondeur
Branche par branche
Naturellement récursif
30
Parcours en largeur
2
4
5
1
3
7
8
9
123456789
6
31
Parcours en largeur (itératif)
Algorithme
Donnée
: ParcoursLargeurGD(a: arbre) (itératif avec file)
: L'arbre a parcouru Variable locale : La file auxiliaire f
début
si EstArbreVide(a) alors retourner Initialiser File(f)
$Enfiler(f,a)$
tant que non EstFileVide(f) faire
$a\leftarrow Defiler(f)$
// c'est ici que l'on fait qqch avec le nœud courant
si non $EstArbreVide(a\rightarrow sag)$ alors $Enfiler(f,a\rightarrow sag)$
si non $EstArbreVide(a\rightarrow sad)$ alors $Enfiler(f,a\rightarrow sad)$
fin
fin
32
Parcours en largeur
2
4
5
1
3
7
8
9
123456789
98765432
6
1
33
Parcours en largeur
☐
Implémentation récursive ?
☐ Sans lien direct entre frères, ça parait difficile !
☐ Pour parcourir de droite à gauche ?
☐
☐
☐ Deux instructions à permuter !
Pour généraliser à un arbre n-aire ?
A chaque itération de la boucle
Défiler le nœud courant
Enfiler tous ses successeurs directs
34
Parcours en profondeur
☐
☐
Conception naturellement récursive
☐ Série de trois instructions
☐ Traitement du nœud courant (le parent) Appels récursif sur ses deux enfants
On distingue trois types de parcours ☐ Selon l'ordre de ces trois instructions
Pré-ordre (ou préfixe): parent puis enfants
In-ordre (ou infixe): premier enfant, parent, puis second enfant Post-ordre (ou postfixe): enfants puis parent
35
Parcours en profondeur pré-ordre (préfixe)
parent puis enfants
2
4
5
1
3
7
8
9
124578369
6
36
Parcours en profondeur in-ordre (infixe)
premier enfant, parent,
puis second enfant
1
2
4
5
3
7
8
9
427581396
6
37
Parcours en profondeur post-ordre (postfixe)
enfants puis parent
2
4
5
1
3
7
8
9
478529631
6
38
Parcours en profondeur (récursif)
Algorithme Donnée
début
: Parcours Préordre (a: arbre) (récursif)
: L'arbre a parcouru
si Est Arbre Vide(a) alors retourner
// c'est ici que l'on fait qqch avec le nœud courant a
Parcours Préordre(a → sag)
Parcours Préordre $(a\rightarrow sad)$
fin
39
Parcours en profondeur (itératif)
Algorithme : Parcours Profondeur Préordre(a: arbre) (itératif avec pile)
Donnée
Variable locale
début
: L'arbre a parcouru
: La pile auxiliaire p
si Est Arbre Vide(a) alors retourner
Initialiser Pile(p)
Empiler(p, a)
tant que non EstPileVide(p) faire
$a\leftarrow Depiler(p)$
// c'est ici que l'on fait qqch avec le nœud courant
si non EstArbre Vide (a → sad) alors $Empiler(p,a\rightarrow sad)$
si non $EstArbreVide(a\rightarrow sag)$ alors $Empiler(p,a\rightarrow sag)$
// Pour faire du post-ordre: permuter les deux dernières instructions
fin
fin
40
Parcours en profondeur
2
4
5
1
3
7
8
9
124578369
7
8
9
6
41
Algorithmes sur Arbre Binaire
Quelques exemples d'algorithmes
Compter le nombre d'éléments d'un AB Libérer la mémoire occupée par un arbre
Mesurer la hauteur d'un AB
Créer un arbre parfait de hauteur n dont les nœuds contiennent respectivement $1,2,...,2^{n+1}-1$ , suivant un parcours en largeur Soient deux adresses de nœuds
Vérifier qu'ils forment branche
i.e. que le premier est l'ancêtre du second
Retourner cette branche sous forme de LSC
43
Compter le nombre d'éléments
Algorithme : NombreElements(a: arbre): entier (récursif)
: L'arbre a dont on compte les éléments : le nombre d'éléments de a
Donnée
Résultat
début
si Est Arbre Vide(a) alors retourner (0
sinon retourner 1 + NombreElements(a → sag) + NombreElements(a → sad)
fin
44
Libérer la mémoire
Algorithme : Libérer(a: arbre)
Donnée modifiée: L'arbre a que l'on libère début
fin
si non EstArbreVide(a) alors
fin
$Liberer(a\rightarrow sag)$
$Liberer(a\rightarrow sad)$
libérer a
45
Mesurer la hauteur
Algorithme : Hauteur(a: arbre)
Donnée
Variable locale
Résultat
début
: L'arbre a que l'on mesure
: $h_{g}$ et $h_{d}$, les hauteurs respectives des fils gauche et droit : La hauteur de a
si EstArbre Vide(a) alors retourner 0 sinon
hg Hauteur $(a\rightarrow sag)$
$h_{d}\leftarrow Hauteur(a\rightarrow sad)$
si $h_{g}>h_{d}$ alors retourner sinon retourner $1+h_{d}$
$1+h_{g}$
fin
fin
46
Créer un arbre parfait
Algorithme : Nouvel Arbre Parfait (n: entier naturel, e: entier positif)
Variable locale : L'arbre parfait a à créer
Donnée
Donnée
Résultat
début
: La hauteur n de a
: L'élément e à stocker dans le nœud racine de a : α
fin
// Note: appel initial Nouvel Arbre Parfait(n, 1) a Créer Noeud (e)
sin $n>0$ alors
fin
a → sag Nouvel Arbre Parfait $fait(n-1,2\times e)$
a
sad
Nouvel Arbre Parfait $fait(n-1,2\times e+1)$
retourner a
47
Vérifier la branche
Le problème peut être reformulé
Vérifier que le second nœud représente un sous-arbre de l'arbre représenté
par le premier
Algorithme
Donnée
Résultat
début
fin
: EstSous Arbre De(a, b: arbre): booleéen
: Deux arbres a et b dont on vérifie que le $2^{d}$ est sous-arbre du $1^{er}$ : Un booléen vrai ssi b est sous-arbre de a
si EstArbreVide(a) ou EstArbre Vide(b) alors retourner faux si $a=b$ alors retourner vrai
retourner EstSous Arbre De(a → sag, b) ou EstSous Arbre De(a → sad, b)
48
Construire la branche
L'idée
1. Descendre récursivement dans toutes les branches
Le nœud cible, et seulement lui, initie une liste (la queue)
2. En remontant, compléter par ajout préfixe (tête)
Ssi l'un des deux fils n'a pas retourné une liste nulle
49
Construire
la branche
Algorithme
Retourner Branche (a,b: arbre): liste
Donnée
: Un arbre a et b l'un de ses sous-arbres
Variable locale
: La liste retournée par l'un des deux appels
Variable locale
: La liste m qui représente le maillon construit à l'échelon local
Résultat
: La branche (a, b) sous forme de LSC, i.e. m
début
fin
// Cas d'initialisation de la branche (sa queue)
si $a=b$ alors
fin
m réserver maillon
$m\rightarrow info\leftarrow a\rightarrow info$
$m\rightarrow succ\leftarrow\emptyset$
retourner m
// On appelle, sinon, récursivement sur le fils gauche, puis le fils droit
si non $EstArbreVide(a\rightarrow sag)$ alors l Retourner Branche $(a\rightarrow sag,b)$
sil $l=\emptyset$ alors
si non EstArbreVide(a → sad.) alors Retourner Branche $(a\rightarrow sad,b)$ fin
// pour, seulement si l'un d'entre eux possède bien b comme sous-arbre :
sil $l=\emptyset$ alors retourner Ø
// compléter le travail :
m réserver maillon
$m\rightarrow info\leftarrow a\rightarrow info$
$m\rightarrow succ\leftarrow l$
retourner m
50
Arbre Binaire de
Recherche
Arbre Binaire de Recherche (ABR)
C'est un Arbre Binaire tel que pour tout nœud a
$max(sag(a))\le a\le min(sad(a))$ (ordre croissant)
$max(sad(a))\le a\le min(sag(a))$ (ordre décroissant)
La relation porte sur les éléments des nœuds et non pas sur les adresses
Il s'agit d'une relation d'ordre (bon ordre)
Elle en induit une par niveau
Les frères sont bien ordonnés
Si on impose <, relation d'ordre totale
52
ABR
10
15
1
11
30
50
35
60
53
Non ABR
10
15
1
16
30
50
35
60
54
Rechercher un élément
Simple dichotomie
Plus besoin d'algorithme récursif et couteux
Une boucle d'itération suffit
Gain: $O(n)\rightarrow O(logn)$ en moyenne
Mais on retombe en $O(n)$
si l'arbre est totalement déséquilibré (~parcours de liste)
55
Illustration : on recherche 11
10
15
1
11
30
$11<10$ ? F
D
50
35
60
56
L'algorithme (version récursive)
Si l'on souhaite compter le nombre d'occurrences
Ajouter un compteur
Si ordre strict, c'est inutile
: Recherche ABR(a: ABR, e: T)
Algorithme
: L'ABR a dans lequel on effectue la recherche : L'élément e recherché
Donnée
Donnée
: un booléen vrai ssi e est un élément de a
Résultat
début
si EstArbreVide(a) alors retourner faux
si $a\rightarrow info=e$ alors retourner vrai
sie $e<a\rightarrow info$ alors Recherche ABR(a → sag, e)
sinon Recherche ABR(a → sad, e)
fin
57
L'algorithme (version itérative)
Algorithme : Recherche ABR(a: ABR, e: T) (itératif)
Donnée
Donnée
Résultat
début
: L'ABR a dans lequel on effectue la recherche : L'élément e recherché
: un booléen vrai ssi e est un élément de a
tant que non EstArbreVide(a) faire
fin
fin
si $a\rightarrow info=e$ alors retourner vrai
si $e<a\rightarrow info$ alors $a\leftarrow a\rightarrow sag$
sinon
$a\leftarrow a\rightarrow sad$
retourner faux
58
Ajouter un élément
Ajout au niveau des feuilles
1. Si l'arbre est vide, on créée une racine
2. Sinon on itère jusqu'au point d'insertion
Place vide sag ou sad dont on mémorise le parent On crée le nœud et on l'insère
C'est donc une adaptation de la recherche
59
Ajouter un élément
Algorithme : AjoutABR(a: ABR, e: T)
Donnée modifiée : L'ABR a dans lequel on effectue l'ajout Variable locale : Une variable b pour itérer a (en donnée modifiée) Variable locale
Donnée
début
fin
: L'adresse p du parent du point d'insertion : L'élément e à ajouter
si Est ArbreVide(a) alors a Nouveau Noeud(e) sinon
fin
$b\leftarrow a$
tant que non EstArbreVide(b) faire $p\leftarrow b$
fin
sie $e<b\rightarrow info$ alors $b\leftarrow b\rightarrow sag$ sinon $b\leftarrow b\rightarrow sad$
b Nouveau Noeud(e)
sie $e<p\rightarrow info$ alors $p\rightarrow sag\leftarrow b$
sinon $p\rightarrow sad\leftarrow b$
60
6
Ajouter un élément: exemple
Construction d'un ABR par ajouts successifs des valeurs 14, 10, 35, 6, 30, 33, 11, 16, 8 et 18
14
10
14
10
30
35
14
6
10
10
14
14
10
35
6
35
10
14
14
30
6
11
30
33
33
35
35
61
Ajouter un élément: exemple
Construction d'un ABR par ajouts successifs des valeurs 14, 10, 35, 6, 30, 33, 11, 16, 8 et 18
10
14
35
10
14
35
10
14
6
11
30
6
11
30
6
11
30
16
33
8
16
33
8
16
33
18
35
62
Supprimer un élément
Π
A) Pour supprimer une feuille, RAS
B) Pour supprimer un nœud à un seul enfant
Raccorder l'enfant en lieu et place du parent supprimé
C) Sinon, c'est un peu plus compliqué, mais à peine
Soit a le nœud à supprimer et :
$m=max(a\rightarrow sag)$, $M=min(a\rightarrow sad)$
Observons que met M ne peuvent avoir deux enfants !!!
1. Permuter la valeur du nœud à supprimer avec m ou avec M La structure d'ABR est préservée !!!
2. Supprimer celui de m ou M qu'on a permuté avec a
Ο
On se ramène à l'un des deux cas A) ou Β) !!!
63
Supprimer un élément : illustration
Le cas C)
6
7
9
6
9
6
9
64
Supprimer un élément : exemple
Le cas A)
7
le noeud n'a pas de fils: décrochage
22
29
34
50
66
71
17
25
32
37
56
70
81
9
21 23 28 30
36 44 55
68
80 97
8 16
27
31
35
52
67 69
94
26
51
88
65
Supprimer un élément : exemple
Le cas A)
le noeud n'a pas de fils: décrochage
7
22
29
34
50
66
71
17
25
32
37
56
70
81
9
21 23 28 30
36 44 55
68
80 97
8 16
27
31
35
52
69
94
26
51
88
66
Supprimer un élément : exemple
Le cas A)
8
18
33
8
18
33
6
16
30
42
6
16
30
42
11
38
10
14
40
10
11
38
40
67
Supprimer un élément : exemple
Le cas B)
le noeud a un seul fils: décrochage
7
22
29
34
50
66
71
17
25
32
37
56
70
81
9 21 23 28
30
36 44 55
68
80 97
8 16
27
31
35
52
69
94
26
51
88
68
Supprimer un élément : exemple
Le cas B)
le noeud a un seul fils: décrochage
7
22
29
34
50
66
71
17
25
32
37
56
70
81
9
21 23 28
30
36 44 55
68
80 97
8 16
27
31
35
52
69
94
26
51
88
69
Supprimer un élément : exemple
Le cas B)
le noeud a un seul fils: décrochage
22
29
34
66
17
50
71
9
21
25
32
37
56
70
81
8 16
23 28
30
36 44 55
68
80 97
27
31
35
52
26
51
69
94
88
70
Supprimer un élément : exemple
Le cas B)
8
18
33
8
18
33
6
16
30
42
6
16
30
42
11
38
11
10
14
40
10
14
40
71
Supprimer un élément : exemple
Le cas C)
le noeud a deux fils
34
17
22
29
50
57
a supprimer
71
9 21
25
32
37
56
70
81
8 16
23 28 30
36 44 55
68
80 97
27
31
35
52
26
51
69
94
88
plus petit
des plus grands
72
Supprimer un élément : exemple
Le cas C)
(deux fils): copie du plus petit des plus grands
34
17
22
29
50
57
71
9 21
25
32
37
56
70
81
8 16
23 28 30
36 44 55
68
80 97
27
31
35
52
26
51
69
94
88
73
Supprimer un élément : exemple
Le cas C)
(deux fils): copie du plus petit des plus grands
34
17
22
29
50
68
71
9 21
25
32
37
56
70
81
8 16
23 28 30
36 44 55
68
80 97
27
31
35
52
26
51
69
94
88
74
Supprimer un élément : exemple
Le cas C)
(deux fils): décrochage
34
17
22
29
50
68
71
9 21
25
32
37
56
70
81
8 16
23 28
30
36 44 55
68
80 97
27
31
35
52
26
51
69
94
88
75
Supprimer un élément : exemple
Le cas C)
(deux fils): décrochage
34
17
22
29
50
68
71
9
21
25
32
37
56
70
81
8 16
23 28
30
36 44 55
69
80 97
27
31
35
52
26
51
94
88
76
Supprimer un élément : exemple
Le cas C)
8
18
33
8
16
33
6
16
30
42
6
11
30
42
11
38
10
14
40
10
14
38
40
77
Arbre Binaire de Recherche : coûts
Structure
insertion
recherche
suppression
tableau
$\mathcal{O}(1)$
$\mathcal{O}(n)$
$\mathcal{O}(n)$
tableau trié
$\mathcal{O}(n)$
$\mathcal{O}(log~n)$
$\mathcal{O}(n)$
liste
$\mathcal{O}(1)$
$\mathcal{O}(n)$
$\mathcal{O}(n)$
ABR
$\mathcal{O}(h)$
$\mathcal{O}(h)$
$\mathcal{O}(h)$
où hest la hauteur de l'arbre :
log n dans le meilleur des cas, n dans le pire des cas
78