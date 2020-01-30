import math

class PrintingNeatly(object):
    def __init__(self, n):
        self.__n = n
        self.textLst = []
        self.textPrice = []

    def __call__(self, text):
        self.textLst = text.split(' ')
        self.textPrice = []
        for t in self.textLst:
            self.textPrice.append(len(t))
        return self.__printingNeatly()

    def __price(self, i, j):
        tmp = self.__n - j + i + 1 - sum(self.textPrice[i:j])
        if tmp < 0: return math.inf
        return tmp

    def __printingNeatly(self):
        Nwords = len(self.textLst)
        priceLst = [math.inf for _ in range(Nwords + 1)]
        breakLst = [-1 for _ in range(Nwords)]
        priceLst[Nwords] = 0
        for i in range(Nwords - 1, -1, -1):
            for j in range(i + 1, Nwords + 1):
                newPrice = self.__price(i, j)
                if newPrice == math.inf: break
                if newPrice < priceLst[i]:
                    priceLst[i] = newPrice + priceLst[j]
                    breakLst[i] = j
        print(priceLst)
        print(breakLst)
        return self.__reconstruct(breakLst)

    def __reconstruct(self, breakLst):
        oldIndex = 0
        index = breakLst[0]
        result = []
        while index < len(breakLst):
            line = []
            for i in range(oldIndex, index):
                line.append(self.textLst[i])
            result.append(line)
            oldIndex = index
            index = breakLst[index]
        line = []
        for i in range(oldIndex, len(self.textLst)):
            line.append(self.textLst[i])
        result.append(line)

        string = ""
        for l in result:
            string += ' '.join(l)
            string += '\n'
        return string

pn = PrintingNeatly(15)
print(pn("tuan dep trai qua ahihi bla blah karaoke"))


