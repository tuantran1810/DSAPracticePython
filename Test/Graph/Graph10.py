import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import WeightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = WeightedDirectionAdjacencyMatrix([1, 2, 3, 4, 5, 6])

adj.AddPath(1, 5, -1)
adj.AddPath(2, 1, 1)
adj.AddPath(2, 4, 2)
adj.AddPath(3, 2, 2)
adj.AddPath(3, 6, -8)
adj.AddPath(4, 1, -4)
adj.AddPath(4, 5, 3)
adj.AddPath(5, 2, 7)
adj.AddPath(6, 2, 5)
adj.AddPath(6, 3, 10)

alg = GraphAlgorithms(adj)
L, pi = alg.AllPairsExtendedShortestPath()
print(L)
print(pi)
print("=" * 50)
L = alg.FastAllPairsExtendedShortestPath()
print(L)
