import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import WeightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = WeightedDirectionAdjacencyMatrix([1, 2, 3, 4, 5])

adj.AddPath(1, 2, 3)
adj.AddPath(1, 3, 8)
adj.AddPath(1, 5, -4)
adj.AddPath(2, 4, 1)
adj.AddPath(2, 5, 7)
adj.AddPath(3, 2, 4)
adj.AddPath(4, 1, 2)
adj.AddPath(4, 3, -5)
adj.AddPath(5, 4, 6)

alg = GraphAlgorithms(adj)
L, pi = alg.AllPairsExtendedShortestPath()
print(L)
print(pi)
