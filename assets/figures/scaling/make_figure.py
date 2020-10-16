import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import factorial


def nCk(n: int, k: int) -> int:
    f = factorial
    return f(n) / (f(n - k) * f(k))


def n_dets(nelecas: int, ncas: int) -> int:
    return nCk(ncas, nelecas // 2) ** 2


#
# RMACC Stats
#

summit_mem = 460 * 24 * 4.84 + 5 * 48 * 42.7 + 20 * 200
print(f"Summit Memory {summit_mem*10**9:.2e} (Bytes)")

water = plt.imread("water.png")
server = plt.imread("server_rack.png")
laptop = plt.imread("laptop.png")


#
# Plot
#
plt.figure()
sns.set_style("darkgrid")
sns.set_palette("muted")

# Plot scaling
x = np.arange(8, 28, 2)
y = np.array([n_dets(i, i) for i in x]) * 8

for i, xi in enumerate(x):
    print(f"{xi} -> {y[i]:.2e}")


# Plot images

ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.imshow(water, extent=(8, 12, 2, 6))
ax2.imshow(water, extent=(18, 22, 2, 6))
ax2.imshow(water, extent=(18, 22, 3, 7))

ax2.imshow(laptop, extent=(17, 19, -5, -3))

ax2.imshow(server, extent=(19, 21, -3, -1))

ax2.text(24, 0, "RMACC Summit\nSupercomputer", ha="center")

# ax2.imshow(server, extent=(21.5, 22.5, 0, 1))
# ax2.imshow(server, extent=(21.5, 22.5, 1, 2))

ax2.set_ylim((-5, 5))
ax2.axis("off")
ax1.semilogy(x, y, "o-")
ax1.set_xticks(np.arange(8, 28, 4))
plt.title("Memory Cost of FCI Wave Functions", fontsize=15)
ax1.set_ylabel("Size of Wave Function (Bytes)")
ax1.set_xlabel("Number of correlated electrons/orbitals")
plt.savefig("scaling.png", dpi=900)


#
# Calc. Hilbert Space size for several systems
#
print("\n\n")
print(f"Hilbert Space Size CAS(18e,18o) = {n_dets(18,18):.2e}")
print(f"Hilbert Space Size CAS(22e,22o) = {n_dets(22,22):.2e}")


# FeP
print(f"Hilbert Space Size CAS(32e,29o) = {n_dets(32,29):.2e}")
print(f"Hilbert Space Size CAS(44e,44o) = {n_dets(44,44):.2e}")

# p-benzyne
print(f"Hilbert Space Size CAS(28e,28o) = {n_dets(28,28):.2e}")

# Fe(PDI)
print(f"Hilbert Space Size CAS(24e,21o) = {n_dets(24,21):.2e}")
print(f"Hilbert Space Size CAS(36e,36o) = {n_dets(36,36):.2e}")

