import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import WeightedIndirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = WeightedIndirectionAdjacencyMatrix(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

adj.AddPath('a', 'b', 4)
adj.AddPath('a', 'h', 8)
adj.AddPath('b', 'h', 11)
adj.AddPath('b', 'c', 8)
adj.AddPath('h', 'g', 1)
adj.AddPath('h', 'i', 7)
adj.AddPath('i', 'g', 6)
adj.AddPath('i', 'c', 2)
adj.AddPath('c', 'd', 7)
adj.AddPath('c', 'f', 4)
adj.AddPath('g', 'f', 2)
adj.AddPath('d', 'f', 14)
adj.AddPath('d', 'e', 9)
adj.AddPath('f', 'e', 10)

alg = GraphAlgorithms(adj)
result = alg.MST_Kruskal()
print(result)
print("=" * 50)
result = alg.MST_Prim()
print(result)
