import math
import sys
sys.path.insert(0, './../../Graph/')
from Graph import WeightedDirectionAdjacencyMatrix

class DAGLongestPath(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __call__(self, s, t):
        path = {}
        for v in self.matrix.AllVertexes():
            path[(v, v)] = 0
        return self.__longestPath(s, t, path)

    def __longestPath(self, s, t, path):
        if (s, t) in path: return path[(s, t)]
        choosen = - math.inf
        for v, _ in self.matrix.AllSuccessors(s):
            tmp = self.__longestPath(v, t, path)
            pathlength = tmp + self.matrix.GetPath(s, v)
            if pathlength > choosen:
                choosen = pathlength
        path[(s, t)] = choosen
        return choosen

matrix = WeightedDirectionAdjacencyMatrix()

matrix.AddPath(1, 2, 1)
matrix.AddPath(1, 3, 1)
matrix.AddPath(1, 4, 1)
matrix.AddPath(2, 3, 1)
matrix.AddPath(2, 4, 1)
matrix.AddPath(3, 4, 1)
matrix.AddPath(4, 5, 1)

longestPath = DAGLongestPath(matrix)
print(longestPath(1, 5))

