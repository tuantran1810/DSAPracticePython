import sys
sys.path.insert(0, './../DataStructures/')
from Graph import AdjacencyMatrix
from LinkedList import Queue

class GraphAlgoritms():
    def __init__(self, adjacencyMatrix):
        if adjacencyMatrix is None:
            raise Exception("invalid input param")
        self.__adjacencyMatrix = adjacencyMatrix

    def BreadthFirstSearch(self, vertex):
        if not self.__adjacencyMatrix.CheckVertexExist(vertex):
            raise Exception("node not exist in graph")
        queue = Queue()
        distance = {}
        predecessor = {}
        layer = {}
        layerCnt = 0

        visited = set()
        visited.add(vertex)
        queue.Enqueue(None)
        queue.Enqueue(vertex)
        queue.Enqueue(None)
        distance[vertex] = 0
        predecessor[vertex] = None
        layer[0] = [vertex]

        while(len(queue) > 0):
            v, _ = queue.Dequeue()
            if v is None:
                if len(layer[layerCnt]) > 0:
                    layerCnt += 1
                    layer[layerCnt] = []
                continue
            for av, dis in self.__adjacencyMatrix.AllSuccessors(v):
                if av in visited: continue
                visited.add(av)
                distance[av] = distance[v] + dis
                predecessor[av] = v
                queue.Enqueue(av)
                layer[layerCnt].append(av)
            queue.Enqueue(None)
        return (distance, predecessor, layer)

adj = AdjacencyMatrix(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])

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

print(adj)

alg = GraphAlgoritms(adj)
distance, predecessor, layer = alg.BreadthFirstSearch('a')
print(distance)
print(predecessor)
print(layer)
