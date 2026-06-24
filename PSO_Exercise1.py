from PVector import *
import math
import copy


class Particle:
    def __init__(self, x=None, y=None, range_positions=(0, 10)):
        if x is None or y is None:
            self.X_actual = PVector(range=range_positions)
        else:
            self.X_actual = PVector(x, y)

        self.X_best = copy.deepcopy(self.X_actual)
        self.Vi = PVector(1, 1)
        self.best_score = float("inf")

    def move(self, c1: float, c2: float, g: PVector):
        # Factor de Constricción de Clerc
        phi = c1 + c2
        K = 2.0 / abs(2.0 - phi - math.sqrt((phi**2) - (4.0 * phi)))

        cognitive = random.random() * c1 * (self.X_best - self.X_actual)
        social = random.random() * c2 * (g - self.X_actual)

        self.Vi = (self.Vi + cognitive + social) * K

        self.X_actual += self.Vi


class Population:
    def __init__(self, fitnessFunction, sizePop=100, rangePositions=(0, 10)):
        self.globalPos = PVector(range=rangePositions)
        self.particles = [
            Particle(range_positions=rangePositions) for _ in range(sizePop)
        ]
        self.fitnessFunction = fitnessFunction

    def evol(self, c1, c2):
        for P in self.particles:
            P.move(c1, c2, self.globalPos)

            scoreActualPosition = self.fitnessFunction(P.X_actual)

            if scoreActualPosition < P.best_score:
                P.best_score = scoreActualPosition
                P.X_best = P.X_actual

        self.globalPos = min(
            (P.X_best for P in self.particles), key=self.fitnessFunction
        )

    def returnNumbers(self):
        numbersArray = [P.X_actual.x for P in self.particles]
        return numbersArray


"""def fitnessFunction(vector: PVector):
    # Función de costo: minimizar x^2 + y^2
    return math.pow(vector.x - 20, 2) + math.pow(vector.y + 5, 2)


Pop = Population(
    rangePositions=(-100, 100), sizePop=50, fitnessFunction=fitnessFunction
)

for _ in range(100):
    Pop.evol(c1=2.1, c2=2.2)

print(Pop.globalPos)"""
