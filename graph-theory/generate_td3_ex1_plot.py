import matplotlib.pyplot as plt
import numpy as np
import os

def plot_td3_ex1():
    fig, ax = plt.subplots(figsize=(10, 8))

    # X1 range
    x1 = np.linspace(0, 5, 400)
    
    # Constraints in Ox1x4 plane:
    # x2 >= 0 => 2 - x1 + x4 >= 0 => x4 >= x1 - 2
    # x3 >= 0 => 2 - 2x1 + x4 >= 0 => x4 >= 2x1 - 2
    # x1 >= 0
    # x4 >= 0
    
    y1 = x1 - 2
    y2 = 2 * x1 - 2
    
    # Feasible region: x4 >= max(0, x1-2, 2x1-2)
    x_fill = np.linspace(0, 5, 400)
    y_fill_bottom = np.maximum(0, np.maximum(x_fill - 2, 2 * x_fill - 2))
    y_fill_top = np.full_like(x_fill, 8) # Unbounded, we pick an upper limit for display
    
    ax.fill_between(x_fill, y_fill_bottom, y_fill_top, color='yellow', alpha=0.3, label='Domaine Admissible')

    # Boundary lines
    ax.plot(x1, y1, 'b-', label=r'$x_2 = 0 \rightarrow x_4 = x_1 - 2$')
    ax.plot(x1, y2, 'r-', label=r'$x_3 = 0 \rightarrow x_4 = 2x_1 - 2$')

    # Basic solution: (0,0) in Ox1x4
    ax.plot(0, 0, 'go', markersize=10, label='Solution Basique (0,0)')
    ax.text(0.1, 0.1, 'B(0,0)', fontsize=12, fontweight='bold', color='green')

    # Axes
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)

    # Formatting
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 8)
    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_4$', fontsize=12)
    ax.legend(loc='upper left', fontsize=11)
    ax.set_title(r'TD3 Exercice 1 : Domaine Admissible dans le repère $Ox_1x_4$', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)

    output_dir = 'plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(os.path.join(output_dir, 'td3_ex1.png'), bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    plot_td3_ex1()
