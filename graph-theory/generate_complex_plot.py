import numpy as np
import matplotlib.pyplot as plt
import os

def generate_complex_example():
    output_dir = 'graph-theory/plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x = np.linspace(0, 15, 1000)
    
    # Contraintes :
    # (3) 4x1 - 5x2 <= 21 => x2 >= (4x1 - 21) / 5
    # (4) 2x1 + 3x2 <= 30 => x2 <= (30 - 2x1) / 3
    # (5) 3x1 - 2x2 <= 18 => x2 >= (3x1 - 18) / 2
    # (6) -0.5x1 + 3x2 <= 15 => x2 <= (15 + 0.5x1) / 3
    
    y3 = (4*x - 21) / 5
    y4 = (30 - 2*x) / 3
    y5 = (3*x - 18) / 2
    y6 = (15 + 0.5*x) / 3

    plt.figure(figsize=(10, 8))
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)

    # Tracé des droites
    plt.plot(x, y3, label=r'$4x_1 - 5x_2 \leq 21$ (3)', color='red')
    plt.plot(x, y4, label=r'$2x_1 + 3x_2 \leq 30$ (4)', color='blue')
    plt.plot(x, y5, label=r'$3x_1 - 2x_2 \leq 18$ (5)', color='green')
    plt.plot(x, y6, label=r'$-0.5x_1 + 3x_2 \leq 15$ (6)', color='purple')

    # Remplissage du domaine (On trouve les intersections manuellement ou par logique de polygone)
    # Les points d'intersection approximatifs d'après le PDF sont (6,6) etc.
    # On va remplir la zone commune
    d = np.linspace(0, 12, 1000)
    y_min = np.maximum(0, np.maximum(y3, y5))
    y_max = np.minimum(y4, y6)
    
    plt.fill_between(x, y_min, y_max, where=(y_max > y_min), color='gray', alpha=0.3, label='Domaine Admissible')

    # Exemple de fonction objectif (tirée de la page 15 du PDF : Z = 3x1 + 8x2)
    # Z = 66 est l'optimum au point (6, 6)
    z_opt = 3*6 + 8*6 # 66
    plt.plot(x, (66 - 3*x)/8, 'k--', linewidth=2, label=r'Objectif $Z = 3x_1 + 8x_2 = 66$')
    plt.scatter(6, 6, color='black', s=100, zorder=5)
    plt.annotate('Optimum (6, 6)', xy=(6, 6), xytext=(8, 8),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xlim(0, 12)
    plt.ylim(0, 10)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title("Résolution Graphique : Exemple Complexe à 4 Contraintes")
    plt.legend(loc='upper right')
    plt.grid(True, linestyle=':', alpha=0.4)
    
    plt.savefig(f'{output_dir}/exemple_complexe.png')
    plt.close()

if __name__ == "__main__":
    generate_complex_example()
