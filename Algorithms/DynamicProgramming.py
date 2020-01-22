import math

class RodCutting():
    def __init__(self, arr):
        self.__arr = arr
        self.__memo = {}

    def __call__(self, n):
        self.__memo = {}
        price = self.__maxRod(n)
        return price

    def __maxRod(self, n):
        if n == 0: return 0
        if n in self.__memo: return self.__memo[n]
        price = - math.inf
        for i in range (1, len(self.__arr)):
            if n - i < 0: break
            newPrice = self.__arr[i] + self.__maxRod(n - i)
            if newPrice > price:
                price = newPrice
        self.__memo[n] = price
        return price

class RodCuttingBottomUp():
    def __init__(self, arr):
        self.__arr = arr

    def __call__(self, n):
        memo = [- math.inf for _ in range(n + 1)]
        memo[0] = 0
        for j in range(1, n + 1):
            for i in range(1, j + 1):
                if i >= len(self.__arr): break
                newPrice = self.__arr[i] + memo[j - i]
                if newPrice > memo[j]: memo[j] = newPrice
        return memo[-1]

rodCutting = RodCutting([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
maxPrice = rodCutting(500)
print(maxPrice)

rodCutting = RodCuttingBottomUp([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
maxPrice = rodCutting(500)
print(maxPrice)
