from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4 6]

class Scattering:
    x = 0

    def __init__(self, data):
        self.x = data

    def Avg(self):
        avg = mean(self.x)
        return avg

    def var_sd(self):
        avg = Avg(self.x)
        diff = [(d - avg) ** 2 for d in self.x]
        var = sum(diff) / (len(self.x) - 1)
        sd = sqrt(var)

        return var, sd