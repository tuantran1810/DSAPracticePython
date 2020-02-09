import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import WeightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = WeightedDirectionAdjacencyMatrix(['r', 's', 't', 'x', 'y', 'z'])

adj.AddPath('r', 's', 5)
adj.AddPath('r', 't', 3)
adj.AddPath('s', 'x', 6)
adj.AddPath('s', 't', 2)
adj.AddPath('t', 'x', 7)
adj.AddPath('t', 'y', 4)
adj.AddPath('t', 'z', 2)
adj.AddPath('x', 'y', -1)
adj.AddPath('x', 'z', 1)
adj.AddPath('y', 'z', -2)

alg = GraphAlgorithms(adj)
result = alg.ShortestPathBellmanFord('s')
print(result)
print("=" * 50)
result = alg.ShortestPathDAG('s')
print(result)
