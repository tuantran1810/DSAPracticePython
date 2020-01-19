import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedIndirectionAdjacencyMatrix
from Algorithms import GraphAlgoritms
from LinkedList import Queue, Stack

adj = UnweightedIndirectionAdjacencyMatrix(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'x', 'y', 'z'])

adj.AddPath('a', 'b')
adj.AddPath('a', 'c')
adj.AddPath('b', 'd')
adj.AddPath('b', 'e')
adj.AddPath('d', 'f')
adj.AddPath('e', 'g')
adj.AddPath('e', 'h')
adj.AddPath('g', 'i')
adj.AddPath('g', 'j')
adj.AddPath('h', 'k')
adj.AddPath('i', 'l')
adj.AddPath('j', 'l')
adj.AddPath('y', 'z')
adj.AddPath('y', 'x')

print(adj)

alg = GraphAlgoritms(adj)
print("BFS:")
for v, distance, predecessor, layer in alg.BreadthFirstSearchAll():
    print("Vertex: " + str(v))
    print(distance)
    print(predecessor)
    print(layer)
    print("=" * 50)

print("DFS:")
for v, distance, predecessor in alg.DepthFirstSearchAll():
    print("Vertex: " + str(v))
    print(distance)
    print(predecessor)
    print("=" * 50)

print("Topological DFS:")
lst = []
for v in alg.DFSTopologicalSortVertex('a'):
    lst.append(v)
print(lst)