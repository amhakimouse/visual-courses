import matplotlib.pyplot as plt
import numpy as np
import os

def plot_ex4():
    fig, ax = plt.subplots(figsize=(10, 8))

    # X values for the lines
    x = np.linspace(-1, 7, 400)
    
    # L1: 2x1 - 4x2 = 1  => x2 = 0.5x1 - 0.25  (x3 = 0)
    y1 = 0.5 * x - 0.25
    # L2: 3x1 + 4x2 = 24 => x2 = -0.75x1 + 6   (x4 = 0)
    y2 = -0.75 * x + 6
    # L3: x2 = 4 (x5 = 0)
    # L4: x1 = 5 (x6 = 0)

    ax.plot(x, y1, 'b-', linewidth=2, label='L1: $2x_1 - 4x_2 = 1$ ($x_3=0$)')
    ax.plot(x, y2, 'r-', linewidth=2, label='L2: $3x_1 + 4x_2 = 24$ ($x_4=0$)')
    ax.axhline(4, color='m', linewidth=2, label='L3: $x_2 = 4$ ($x_5=0$)')
    ax.axvline(5, color='g', linewidth=2, label='L4: $x_1 = 5$ ($x_6=0$)')

    # Points for the specific bases
    # B1: x1=0, x2=0
    # B2: L2 (x4=0) and L3 (x5=0) => (8/3, 4)
    # B3: x1=0 and L2 (x4=0) => (0, 6)
    # B4: L1 (x3=0) and L2 (x4=0) => (5, 2.25)
    pts = {
        '$B_1(0,0)$': (0, 0, 'green'),         # SBA
        '$B_2(8/3, 4)$': (8/3, 4, 'green'),    # SBA
        '$B_3(0, 6)$': (0, 6, 'purple'),       # Non-Admissible (x2 <= 4)
        '$B_4(5, 2.25)$': (5, 2.25, 'green')   # SBA (now admissible!)
    }

    for name, (px, py, color) in pts.items():
        ax.plot(px, py, marker='o', color=color, markersize=8, zorder=5)
        ax.text(px + 0.1, py + 0.2, name, fontsize=11, fontweight='bold', color=color)

    # Feasible region vertices
    # (0,0), (0.5, 0), (5, 2.25), (8/3, 4), (0, 4)
    polygon_x = [0, 0.5, 5, 8/3, 0]
    polygon_y = [0, 0, 2.25, 4, 4]
    ax.fill(polygon_x, polygon_y, color='yellow', alpha=0.3, label='Domaine Admissible')

    # Optimum point
    ax.plot(8/3, 4, marker='*', color='gold', markersize=15, markeredgecolor='black', zorder=10, label='Optimum $(8/3, 4)$')

    # Axes
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)

    # Formatting
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_2$', fontsize=12)
    ax.legend(loc='upper right', fontsize=11)
    ax.set_title('Exercice 4 : Domaine Admissible (Corrigé $x_2 \leq 4, x_1 \leq 5$)', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)

    output_dir = 'plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(os.path.join(output_dir, 'td2_ex4.png'), bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    plot_ex4()
