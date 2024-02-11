# First load the numpy/scipy/matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Import hermite polynomials and factorial to use in normalization factor
from scipy.special import hermite
from math import factorial

#Check to see if they match the table
H=hermite(4)
print(H)

x = np.linspace(-2, 2, 1000)  # Range needs to be specified for plotting functions of x

for v in range(0, 3):
    H = hermite(v)

    f = H(x)

    plt.plot(x, f)

plt.xlabel('x')
plt.ylabel(r'$H_n(x)$')


def N(v):
    '''Normalization constant '''

    return 1. / np.sqrt(np.sqrt(np.pi) * 2 ** v * factorial(v))


def psi(v, x):
    """Harmonic oscillator wavefunction for level v computed on grid of points x"""

    Hr = hermite(v)

    Psix = N(v) * Hr(x) * np.exp(-0.5 * x ** 2)

    return Psix

# Check orthogonality

psi(1,x) @ psi(4,x)

# Normalization is computed by using numerical integration with trapezoidal method:
from scipy.integrate import trapz

# remember that x runs form -inf to +inf so lets use large xmin and xmax
x=np.linspace(-10,10,1000)

psi2=psi(5,x)**2

Integral = trapz(psi2,x)

print(Integral)


@widgets.interact(v=(0, 50))
def plot_psi(v=0):
    x = np.linspace(-10, 10, 1000)

    y = psi(v, x) ** 2

    plt.plot(x, y, lw=2)

    plt.grid('on')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('$\psi_n(x)$', fontsize=16)


def E(v):
    '''Eigenvalues in units of h'''

    return (v + 0.5)


def V(x):
    """Potential energy function"""

    return 0.5 * x ** 2

# plot up to level vmax
VMAX=8

# Range of x determine by classical tunring points:
xmin, xmax = -np.sqrt(2*E(VMAX)), np.sqrt(2*E(VMAX))

x = np.linspace(xmin, xmax, 1000)

fig, ax = plt.subplots(figsize=(8, 8))

for v in range(8):
    # plot potential V(x)
    ax.plot(x, V(x), color='black')

    # plot psi squared which we shift up by values of energy
    ax.plot(x, psi(v, x) ** 2 + E(v), lw=2)

    # add lines and labels
    ax.axhline(E(v), color='gray', linestyle='--')
    ax.text(xmax, 1.2 * E(v), f"v={v}")

ax.set_xlabel('x')
ax.set_ylabel('$\psi^2_n(x)$')