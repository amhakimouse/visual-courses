import matplotlib.pyplot as plt
import numpy as np

def plot_ex3():
    fig, ax = plt.subplots(figsize=(10, 7))

    # X values for the lines
    x = np.linspace(-3, 6, 400)
    
    # Line 1: -x1 + x2 = 1  => x2 = x1 + 1 (Occurs when x3 = 0)
    y1 = x + 1
    # Line 2: x1 + 2x2 = 4 => x2 = -0.5*x1 + 2 (Occurs when x4 = 0)
    y2 = -0.5 * x + 2

    ax.plot(x, y1, 'b-', linewidth=2, label='Éq 1: $-x_1 + x_2 = 1$ ($x_3=0$)')
    ax.plot(x, y2, 'r-', linewidth=2, label='Éq 2: $x_1 + 2x_2 = 4$ ($x_4=0$)')

    # Base solutions projected onto Ox1x2
    pts = {
        '$B_{12} (2/3, 5/3)$': (2/3, 5/3, 'green', 'SBA (Admissible)'),
        '$B_{13} (4, 0)$': (4, 0, 'green', ''),
        '$B_{14} (-1, 0)$': (-1, 0, 'purple', 'SB (Non-Admissible)'),
        '$B_{23} (0, 2)$': (0, 2, 'purple', ''),
        '$B_{24} (0, 1)$': (0, 1, 'green', ''),
        '$B_{34} (0, 0)$': (0, 0, 'green', '')
    }

    for name, (px, py, color, label_text) in pts.items():
        ax.plot(px, py, marker='o', color=color, markersize=8, zorder=5)
        ax.text(px + 0.15, py + 0.15, name, fontsize=12, fontweight='bold', color=color)

    # Axes
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)

    # Feasible region (where x1>=0, x2>=0, x3>=0 => x2<=x1+1, x4>=0 => x2<=-0.5x1+2)
    x_fill = np.linspace(0, 4, 400)
    y_top = np.minimum(x_fill + 1, -0.5 * x_fill + 2)
    ax.fill_between(x_fill, 0, y_top, color='yellow', alpha=0.3, label='Domaine Admissible')

    # Formatting
    ax.set_xlim(-2, 5)
    ax.set_ylim(-1, 3)
    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_2$', fontsize=12)
    ax.legend(loc='upper right', fontsize=11)
    ax.set_title('Projections des Solutions de Base dans le repère $Ox_1x_2$', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)

    import os
    if not os.path.exists('graph-theory/plots'):
        os.makedirs('graph-theory/plots')
    plt.savefig('graph-theory/plots/td2_ex3.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    plot_ex3()
