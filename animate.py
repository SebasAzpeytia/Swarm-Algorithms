import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PSO_Exercise1 import *
from PVector import *


def fitnessFunctionBasic(vector: PVector):
    # Función de costo: minimizar x^2 + y^2
    return math.pow(vector.x - 20, 2) + math.pow(vector.y - 30, 2)


Pop = Population(
    rangePositions=(-100, 100), sizePop=20, fitnessFunction=fitnessFunctionBasic
)

fig, ax = plt.subplots()

ax.set(xlim=(-100, 100), ylim=(-100, 100))

dispersion = ax.scatter([], [], zorder=1)
ax.scatter([20], [30], c="r", zorder=3)


def update(frame):
    Pop.evol(c1=2.1, c2=2.1)
    positions = np.array([[P.X_actual.x, P.X_actual.y] for P in Pop.particles])

    dispersion.set_offsets(positions)

    return (dispersion,)


ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=10, blit=True)

plt.show()
