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

class ExtendedRodCutting():
    def __init__(self, arr):
        self.__arr = arr
        self.__memo = {}
        self.__path = []

    def __call__(self, n):
        self.__memo = {}
        self.__path = []
        price = self.__maxRod(n)
        path = self.__getPath(self.__path)
        return (price, path)

    def __maxRod(self, n):
        if n == 0: return 0
        if n in self.__memo: return self.__memo[n]
        price = - math.inf
        k = -1
        for i in range (1, len(self.__arr)):
            if n - i < 0: break
            newPrice = self.__arr[i] + self.__maxRod(n - i)
            if newPrice > price:
                price = newPrice
                k = i
        self.__memo[n] = price
        self.__path.append(k)
        return price

    def __getPath(self, path):
        result = []
        n = len(path) - 1
        while n > 0:
            result.append(path[n])
            n -= path[n]
        return result

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

class ExtendedRodCuttingBottomUp():
    def __init__(self, arr):
        self.__arr = arr

    def __call__(self, n):
        memo = [- math.inf for _ in range(n + 1)]
        memo[0] = 0
        path = [-1 for _ in range(n + 1)]
        path[0] = 0
        for j in range(1, n + 1):
            for i in range(1, j + 1):
                if i >= len(self.__arr): break
                newPrice = self.__arr[i] + memo[j - i]
                if newPrice > memo[j]:
                    memo[j] = newPrice
                    path[j] = i
        return (memo[-1], self.__getPath(path))

    def __getPath(self, path):
        result = []
        n = len(path) - 1
        while n > 0:
            result.append(path[n])
            n -= path[n]
        return result

rodCutting = RodCutting([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
maxPrice = rodCutting(500)
print(maxPrice)

rodCutting = ExtendedRodCutting([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
maxPrice = rodCutting(4)
print(maxPrice)

rodCutting = RodCuttingBottomUp([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
maxPrice = rodCutting(500)
print(maxPrice)

rodCutting = ExtendedRodCuttingBottomUp([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
maxPrice = rodCutting(4)
print(maxPrice)
