import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import WeightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = WeightedDirectionAdjacencyMatrix(['s', 't', 'x', 'y', 'z'])

adj.AddPath('s', 't', 10)
adj.AddPath('s', 'y', 5)
adj.AddPath('t', 'y', 2)
adj.AddPath('t', 'x', 1)
adj.AddPath('x', 'z', 4)
adj.AddPath('y', 't', 3)
adj.AddPath('y', 'x', 9)
adj.AddPath('y', 'z', 2)
adj.AddPath('z', 's', 7)
adj.AddPath('z', 'x', 6)

alg = GraphAlgorithms(adj)
result = alg.ShortestPathDijsktra('s')
print(result)
