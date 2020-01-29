import math

class OptimalBST():
    def __call__(self, p, q, n):
        """
        p: probability of a node (array of index 0...n with index 0 left blank)
        q: probability of a dummy node (array of index 0...n)
        n: number of nodes, 1...n
        """
        e = [[0 for _ in range(n + 1)] for _ in range(n + 2)]
        w = [[0 for _ in range(n + 1)] for _ in range(n + 2)]
        root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 2):
            e[i][i - 1] = q[i - 1]
            w[i][i - 1] = q[i - 1]
        for l in range(1, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                e[i][j] = math.inf
                w[i][j] = w[i][j - 1] + p[j] + q[j]
                for r in range(i, j + 1):
                    t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r
        return (e, w, root)

e, w, root = OptimalBST()([0, 0.15, 0.10, 0.05, 0.10, 0.20],
    [0.05, 0.10, 0.05, 0.05, 0.05, 0.10], 5)
print(e)
print(w)
print(root)

print('=' * 50)
e, w, root = OptimalBST()([0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14],
    [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05], 7)
print(e)
print(w)
print(root)
