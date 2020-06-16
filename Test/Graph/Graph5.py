import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = UnweightedDirectionAdjacencyMatrix(['D', 'I', 'G', 'S', 'L'])
adj.AddPath('D', 'G')
adj.AddPath('I', 'G')
adj.AddPath('I', 'S')
adj.AddPath('G', 'L')

alg = GraphAlgorithms(adj)
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