import matplotlib.pyplot as plt
import numpy as np

# Définition des intervalles
p1 = np.linspace(0, 12, 100)
p2 = np.linspace(12, 12.5, 100)
p3 = np.linspace(12.5, 20, 100)

# Définition des fonctions de profit
z1 = 2750 - 105 * p1
z2 = 2690 - 100 * p2
z3 = np.full_like(p3, 1440)

plt.figure(figsize=(10, 6))

# Tracé des segments
plt.plot(p1, z1, label='$Z = -105p + 2750$ ($0 \leq p \leq 12$)', color='blue', linewidth=2)
plt.plot(p2, z2, label='$Z = -100p + 2690$ ($12 \leq p \leq 12.5$)', color='green', linewidth=2)
plt.plot(p3, z3, label='$Z = 1440$ ($p \geq 12.5$)', color='red', linewidth=2)

# Points de jonction
plt.scatter([12, 12.5], [1490, 1440], color='black', zorder=5)
plt.annotate('(12, 1490)', (12, 1490), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate('(12.5, 1440)', (12.5, 1440), textcoords="offset points", xytext=(20,10), ha='center')

plt.title('Profit maximal Z en fonction du prix supplémentaire unitaire p')
plt.xlabel('Prix supplémentaire unitaire (p)')
plt.ylabel('Profit maximal (Z)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

plt.savefig('plots/td3_ex7.png')
print("Plot saved to plots/td3_ex7.png")
