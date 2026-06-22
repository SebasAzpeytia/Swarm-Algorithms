import random

class PVector:
    pass

class PVector:
    def __init__(self, x = None, y = None, range = (0,1)):
        if x or y is None:
            self.generateRandomPosition(range[0], range[1])
        else:
            self.x = x
            self.y = y

    def generateRandomPosition(self, min, max):
        self.x = random.uniform(min,max)
        self.y = random.uniform(min,max)
    
    def setVector(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector:PVector):
        return PVector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector:PVector):
        return PVector(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, scalar:float):
        return PVector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def __str__(self):
        return f'({round(self.x, 3)},{round(self.y, 3)})'
