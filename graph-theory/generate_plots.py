import numpy as np
import matplotlib.pyplot as plt
import os

def generate_step_plots():
    output_dir = 'graph-theory/plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x = np.linspace(0, 4, 400)
    y1 = 3 - x
    y2 = 1 + x

    def base_plot():
        plt.figure(figsize=(8, 6))
        plt.axhline(0, color='black', lw=1)
        plt.axvline(0, color='black', lw=1)
        # Domaine
        x_f1 = np.linspace(0, 1, 100)
        plt.fill_between(x_f1, 0, 1 + x_f1, color='yellow', alpha=0.3)
        x_f2 = np.linspace(1, 2, 100)
        plt.fill_between(x_f2, 0, 3 - x_f2, color='yellow', alpha=0.3)
        # Contraintes
        plt.plot(x, y1, 'r--', alpha=0.5, label=r'$x_1+x_2 \leq 3$')
        plt.axvline(2, color='blue', linestyle='--', alpha=0.5, label=r'$x_1 \leq 2$')
        plt.plot(x, y2, 'g--', alpha=0.5, label=r'$-x_1+x_2 \leq 1$')
        plt.xlim(0, 3.5); plt.ylim(0, 3.5)
        plt.xlabel('x1'); plt.ylabel('x2')
        plt.grid(True, linestyle=':', alpha=0.4)

    # Étape 1 : Domaine Admissible seul
    base_plot()
    plt.title("Étape 1 : Identification du Domaine Admissible")
    plt.legend()
    plt.savefig(f'{output_dir}/step1_domaine.png')
    plt.close()

    # Étape 2 : Introduction de Z = 0
    base_plot()
    z_line = -0.5 * x - 0.5 * 0
    plt.plot(x, z_line, 'k:', label='Z = 0 (Départ)')
    plt.title("Étape 2 : Tracé de la ligne objectif initiale (Z=0)")
    plt.legend()
    plt.savefig(f'{output_dir}/step2_z0.png')
    plt.close()

    # Étape 3 : Translation de la ligne
    base_plot()
    for lvl in [0, -2, -4]:
        plt.plot(x, -0.5*x - 0.5*lvl, 'gray', linestyle=':', alpha=0.6)
    plt.arrow(0.5, 0.5, 0.3, 0.6, head_width=0.1, head_length=0.1, fc='blue', ec='blue', label='Sens du déplacement')
    plt.title("Étape 3 : Glissement parallèle vers l'optimum")
    plt.legend()
    plt.savefig(f'{output_dir}/step3_translation.png')
    plt.close()

    # Étape 4 : Point Optimal
    base_plot()
    plt.plot(x, -0.5*x - 0.5*(-5), 'black', linewidth=3, label='Z = -5 (OPTIMUM)')
    plt.scatter(1, 2, color='red', s=100, zorder=5)
    plt.annotate('Optimum (1, 2)', xy=(1, 2), xytext=(1.5, 2.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.title("Étape 4 : Dernier point de contact = Solution Optimale")
    plt.legend()
    plt.savefig(f'{output_dir}/step4_optimum.png')
    plt.close()

if __name__ == "__main__":
    generate_step_plots()
