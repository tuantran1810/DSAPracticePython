import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = UnweightedDirectionAdjacencyMatrix(['y', 'z', 's', 't', 'x', 'w', 'v', 'u'])

adj.AddPath('y', 'x')
adj.AddPath('z', 'y')
adj.AddPath('z', 'w')
adj.AddPath('s', 'z')
adj.AddPath('s', 'w')
adj.AddPath('t', 'v')
adj.AddPath('t', 'u')
adj.AddPath('x', 'z')
adj.AddPath('w', 'x')
adj.AddPath('v', 's')
adj.AddPath('v', 'w')
adj.AddPath('u', 'v')
adj.AddPath('u', 't')

alg = GraphAlgorithms(adj)

print("DFS:")
result = alg.DepthFirstSearchTime()
print(result)

print("Topological DFS:")
lst = []
for v in alg.DFSTopologicalSortAll():
    lst.append(v)
print(lst)

print("Topological BFS:")
lst = []
for v in alg.BFSTopologicalSortAll():
    lst.append(v)
print(lst)
