import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import WeightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = WeightedDirectionAdjacencyMatrix(['s', 't', 'x', 'y', 'z'])

adj.AddPath('s', 't', 6)
adj.AddPath('s', 'y', 7)
adj.AddPath('t', 'y', 8)
adj.AddPath('t', 'z', -4)
adj.AddPath('t', 'x', 5)
adj.AddPath('x', 't', -2)
adj.AddPath('y', 'x', -3)
adj.AddPath('y', 'z', 9)
adj.AddPath('z', 's', 2)
adj.AddPath('z', 'x', 7)

alg = GraphAlgorithms(adj)
result = alg.ShortestPathBellmanFord('s')
print(result)
