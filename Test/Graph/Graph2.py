import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../../Graph/')
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedDirectionAdjacencyMatrix
from GraphAlgorithms import GraphAlgorithms

adj = UnweightedDirectionAdjacencyMatrix(['m', 't', 'q', 'x', 'n', 'u', 'r', 'y', 'o', 'v', 's', 'z', 'p', 'w'])

adj.AddPath('m', 'x')
adj.AddPath('m', 'q')
adj.AddPath('m', 'r')
adj.AddPath('q', 't')
adj.AddPath('n', 'q')
adj.AddPath('n', 'u')
adj.AddPath('n', 'o')
adj.AddPath('u', 't')
adj.AddPath('r', 'u')
adj.AddPath('r', 'y')
adj.AddPath('y', 'v')
adj.AddPath('o', 'r')
adj.AddPath('o', 'v')
adj.AddPath('o', 's')
adj.AddPath('v', 'x')
adj.AddPath('v', 'w')
adj.AddPath('s', 'r')
adj.AddPath('p', 'o')
adj.AddPath('p', 's')
adj.AddPath('p', 'z')
adj.AddPath('w', 'z')

alg = GraphAlgorithms(adj)

print("DFS:")
visited = set()
for v in adj.ZeroInDegreeVertexes():
    distance, predecessor = alg.DepthFirstSearchVertex(v, visited)
    print("Vertex: " + str(v))
    print(distance)
    print(predecessor)
    print("=" * 50)

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
