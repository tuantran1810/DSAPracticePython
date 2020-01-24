class LCSExponentialSolver():
    def __call__(self, strX, strY):
        return self.__lcsLength(strX, strY)

    def __lcsLength(self, strX, strY):
        m = len(strX)
        n = len(strY)
        if m == 0 or n == 0: return 0
        x = strX[-1]
        y = strY[-1]
        # print(f"x = {x}, y = {y}")
        if x == y:
            return self.__lcsLength(strX[0 : (m - 1)], strY[0 : (n - 1)]) + 1
        lcs1 = self.__lcsLength(strX[0 : (m - 1)], strY)
        lcs2 = self.__lcsLength(strX, strY[0 : (n - 1)])
        if lcs1 > lcs2: return lcs1
        return lcs2

class LCSDynamicProgrammingSolver():
    def __init__(self):
        self.strX = ""
        self.strY = ""

    def __call__(self, strX, strY):
        m = len(strX)
        n = len(strY)
        matC = [[(0, None) for _ in range(n + 1)] for _ in range(m + 1)]
        self.strX = strX
        self.strY = strY
        return self.__lcs(strX, strY, matC)

    def __getLCS(self, matC, x, y, arr):
        if x == 0 or y == 0: return
        entry = matC[x][y]
        if x - 1 == entry[1][0] and y - 1 == entry[1][1]:
            arr.append(self.strX[x - 1])
            self.__getLCS(matC, x - 1, y - 1, arr)
        elif x - 1 == entry[1][0] and y == entry[1][1]:
            self.__getLCS(matC, x - 1, y, arr)
        else:
            self.__getLCS(matC, x, y - 1, arr)

    def __lcs(self, strX, strY, matC):
        m = len(self.strX)
        n = len(self.strY)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.strX[i - 1] == self.strY[j - 1]:
                    matC[i][j] = (matC[i - 1][j - 1][0] + 1, (i - 1, j - 1))
                else:
                    lcs1 = matC[i - 1][j][0]
                    lcs2 = matC[i][j - 1][0]
                    if lcs1 > lcs2:
                        matC[i][j] = (matC[i - 1][j][0], (i - 1, j))
                    else:
                        matC[i][j] = (matC[i][j - 1][0], (i, j - 1))
        arr = []
        self.__getLCS(matC, m, n, arr)
        arr.reverse()
        return (matC, ''.join(arr))

lcsExp = LCSExponentialSolver()
result = lcsExp("BDCABA", "ABCBDAB")
print(result)

lcsExp = LCSDynamicProgrammingSolver()
result = lcsExp("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA")
for line in result[0]:
    print(line)
print(result[1])

