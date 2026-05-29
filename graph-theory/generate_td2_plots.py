import matplotlib.pyplot as plt
import numpy as np

def plot_ex1():
    x = np.linspace(0, 10, 400)
    
    # Constraints
    y1 = 2*x + 2
    y2 = x - 2
    y3 = 5 - x
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label=r'$-2x_1 + x_2 \leq 2$')
    plt.plot(x, y2, label=r'$x_1 - x_2 \leq 2$')
    plt.plot(x, y3, label=r'$x_1 + x_2 \leq 5$')
    
    # Feasible region
    y_top = np.minimum(y1, y3)
    y_bottom = np.maximum(0, y2)
    
    plt.fill_between(x, y_bottom, y_top, where=(y_top > y_bottom), color='yellow', alpha=0.3, label='Domaine Admissible')
    
    # Objective function: Min Z = -x1 + x2
    # Z = -x1 + x2 => x2 = x1 + Z
    # Let's plot Z=0 line: x2 = x1
    plt.plot(x, x, '--k', alpha=0.5, label='Z = 0 (-x1 + x2 = 0)')
    
    # Optimum: Min Z
    # Points: (0,0)? (2,0)? (3.5, 1.5)? (1, 4)? (0, 2)?
    # Z(0,0)=0
    # Z(2,0)=-2
    # Intersection L2 and L3: x1-x2=2, x1+x2=5 => 2x1=7 => x1=3.5, x2=1.5. Z=-3.5+1.5=-2.
    # Intersection L1 and L3: -2x1+x2=2, x1+x2=5 => 3x1=3 => x1=1, x2=4. Z=-1+4=3
    # Intersection L1 and x1=0: (0,2). Z=2.
    # Optimum is at (3.5, 1.5) or (2,0)? Wait. x1-x2=2 => x2=x1-2.
    # Actually the segment between (2,0) and (3.5, 1.5) has Z = -x1 + (x1-2) = -2.
    # Let's recheck. Z = -x1 + x2.
    # At (2,0): -2 + 0 = -2.
    # At (3.5, 1.5): -3.5 + 1.5 = -2.
    # Oh, the line Z = -2 is parallel to the boundary x1 - x2 = 2.
    # So multiple optima.
    
    plt.xlim(0, 6)
    plt.ylim(0, 6)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.legend()
    plt.title('TD2 Exercice 1.1 : Min Z = -x1 + x2')
    plt.grid(True)
    plt.savefig('graph-theory/plots/td2_ex1.png')
    plt.close()

def plot_ex2():
    x = np.linspace(0, 15, 400)
    
    # Constraints
    y1 = 6 - x
    # x >= 4 (vertical)
    # y <= 3 (horizontal)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label=r'$x_1 + x_2 \geq 6$')
    plt.axvline(4, color='r', label=r'$x_1 \geq 4$')
    plt.axhline(3, color='g', label=r'$x_2 \leq 3$')
    
    # Feasible region:
    # x2 >= 6 - x1
    # x1 >= 4
    # x2 <= 3
    # If x1=4, x2 >= 2 and x2 <= 3. Range [2, 3].
    # If x1=6, x2 >= 0 and x2 <= 3. Range [0, 3].
    # If x1=10, x2 >= -4 (so 0) and x2 <= 3. Range [0, 3].
    
    xf = np.linspace(4, 15, 400)
    yf_top = np.full_like(xf, 3)
    yf_bottom = np.maximum(0, 6 - xf)
    plt.fill_between(xf, yf_bottom, yf_top, color='yellow', alpha=0.3, label='Domaine (Non-Borné)')
    
    # Objective: Max Z = 5x1 + 7x2
    plt.quiver(5, 1, 5, 7, angles='xy', scale_units='xy', scale=1, color='blue', label='Direction du Gradient Z')
    
    plt.xlim(0, 15)
    plt.ylim(0, 10)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.legend()
    plt.title('TD2 Exercice 1.2 : Max Z = 5x1 + 7x2 (Non-Borné)')
    plt.grid(True)
    plt.savefig('graph-theory/plots/td2_ex2.png')
    plt.close()

def plot_ex3():
    x = np.linspace(0, 10, 400)
    
    # L1: 2x1 - x2 >= -2 => x2 <= 2x1 + 2
    # L2: x1 - 2x2 <= -8 => x2 >= 0.5x1 + 4
    # L3: x1 + x2 <= 5 => x2 <= 5 - x1
    
    y1 = 2*x + 2
    y2 = 0.5*x + 4
    y3 = 5 - x
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label=r'$2x_1 - x_2 \geq -2$')
    plt.plot(x, y2, label=r'$x_1 - 2x_2 \leq -8$')
    plt.plot(x, y3, label=r'$x_1 + x_2 \leq 5$')
    
    plt.xlim(0, 6)
    plt.ylim(0, 7)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.legend()
    plt.title('TD2 Exercice 1.3 : Domaine Vide')
    plt.grid(True)
    
    # No feasible region to fill
    plt.text(2, 6, "Domaine Vide (Inadmissible)", fontsize=12, color='red', fontweight='bold')
    
    plt.savefig('graph-theory/plots/td2_ex3.png')
    plt.close()

if __name__ == "__main__":
    import os
    if not os.path.exists('graph-theory/plots'):
        os.makedirs('graph-theory/plots')
    plot_ex1()
    plot_ex2()
    plot_ex3()
