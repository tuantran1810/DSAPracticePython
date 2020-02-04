import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = UnweightedDirectionAdjacencyMatrix(['u', 'v', 'w', 'x', 'y', 'z'])

adj.AddPath('u', 'v')
adj.AddPath('u', 'x')
adj.AddPath('v', 'y')
adj.AddPath('w', 'y')
adj.AddPath('w', 'z')
adj.AddPath('x', 'v')
adj.AddPath('y', 'x')
adj.AddPath('z', 'z')

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
