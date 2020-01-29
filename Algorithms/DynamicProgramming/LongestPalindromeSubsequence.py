class LongestPalindromeSubsequence(object):
    def __call__(self, string):
        rString = ''.join(reversed(string))
        return self.__longestCommonSubsequence(string, rString)

    def __longestCommonSubsequence(self, strX, strY):
        m = len(strX)
        n = len(strY)
        lengthMatrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        directionMatrix = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if strX[i - 1] == strY[j - 1]:
                    lengthMatrix[i][j] = lengthMatrix[i - 1][j - 1] + 1
                    directionMatrix[i][j] = (i - 1, j - 1)
                    continue
                if lengthMatrix[i - 1][j] > lengthMatrix[i][j - 1]:
                    lengthMatrix[i][j] = lengthMatrix[i - 1][j]
                    directionMatrix[i][j] = (i - 1, j)
                else:
                    lengthMatrix[i][j] = lengthMatrix[i][j - 1]
                    directionMatrix[i][j] = (i, j - 1)
        x, y = m, n
        lcs = []
        while(x != 0 and y != 0):
            newx, newy = directionMatrix[x][y]
            if newx + 1 == x and newy + 1 == y:
                lcs.append(strX[x - 1])
            x, y = newx, newy
        lcs.reverse()
        return ''.join(lcs)

lcsExp = LongestPalindromeSubsequence()
print(lcsExp("character"))
