import matplotlib.pyplot as plt
import numpy as np


def Rosenbrock(x1,x2):
    output = x1**2 +x2**2
    return output

x1 = np.linspace(-2,2,100)
x2 = np.linspace(-2,2,100)

X1, X2 = np.meshgrid(x1, x2)

Z = Rosenbrock(X1,X2)

ax = plt.axes(projection='3d')
ax.plot_surface(X1, X2, Z)
plt.show()