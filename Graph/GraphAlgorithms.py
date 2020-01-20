import sys
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedIndirectionAdjacencyMatrix
from LinkedList import Queue, Stack

class GraphAlgorithms():
    def __init__(self, adjacencyMatrix):
        if adjacencyMatrix is None:
            raise Exception("invalid input param")
        self.__adjacencyMatrix = adjacencyMatrix

    def BreadthFirstSearchVertex(self, vertex, visited = None):
        if vertex is None: raise Exception("input None vertex")
        if not self.__adjacencyMatrix.CheckVertexExist(vertex):
            raise Exception("node not exist in graph")
        queue = Queue()
        distance = {}
        predecessor = {}
        layer = {}
        layerCnt = 0

        if visited is None: visited = set()
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

    def BreadthFirstSearchAll(self):
        visited = set()
        if self.__adjacencyMatrix.IsDigraph():
            for v in self.__adjacencyMatrix.ZeroInDegreeVertexes():
                if v in visited: continue
                distance, predecessor, layer = self.BreadthFirstSearchVertex(v, visited)
                yield v, distance, predecessor, layer
        else:
            for v in self.__adjacencyMatrix.AllVertexes():
                if v in visited: continue
                distance, predecessor, layer = self.BreadthFirstSearchVertex(v, visited)
                yield v, distance, predecessor, layer

    def __depthFirstSearch(self, v, visited, distance, predecessor):
        for av, dis in self.__adjacencyMatrix.AllSuccessors(v):
            if av in visited: continue
            predecessor[av] = v
            distance[av] = distance[v] + 1
            visited.add(av)
            self.__depthFirstSearch(av, visited, distance, predecessor)

    def DepthFirstSearchVertex(self, v, visited = None):
        if v is None: raise Exception("input None vertex")
        if not self.__adjacencyMatrix.CheckVertexExist(v):
            raise Exception("node not exist in graph")
        if visited is None: visited = set()
        distance, predecessor = {}, {}
        visited.add(v)
        distance[v] = 0
        predecessor[v] = None
        self.__depthFirstSearch(v, visited, distance, predecessor)
        return (distance, predecessor)

    def DepthFirstSearchAll(self):
        visited = set()
        if self.__adjacencyMatrix.IsDigraph():
            for v in self.__adjacencyMatrix.ZeroInDegreeVertexes():
                if v in visited: continue
                distance, predecessor = self.DepthFirstSearchVertex(v, visited)
                yield v, distance, predecessor
        else:
            for v in self.__adjacencyMatrix.AllVertexes():
                if v in visited: continue
                distance, predecessor = self.DepthFirstSearchVertex(v, visited)
                yield v, distance, predecessor

    def __dfsTopoSortVertex(self, v, visited, stack):
        if v is None or visited is None or stack is None: raise Exception("invalid input")
        for av, _ in self.__adjacencyMatrix.AllSuccessors(v):
            if av in visited: continue
            visited.add(av)
            self.__dfsTopoSortVertex(av, visited, stack)
        stack.Push(v)

    def DFSTopologicalSortVertex(self, v, visited = None):
        if v is None: raise Exception("input None vertex")
        if not self.__adjacencyMatrix.CheckVertexExist(v):
            raise Exception("node not exist in graph")
        if visited is None: visited = set()
        stack = Stack()
        visited.add(v)
        self.__dfsTopoSortVertex(v, visited, stack)
        while len(stack) > 0:
            v, _ = stack.Pop()
            yield v

    def DFSTopologicalSortAll(self):
        visited = set()
        if self.__adjacencyMatrix.IsDigraph():
            for v in self.__adjacencyMatrix.ZeroInDegreeVertexes():
                if v in visited: continue
                for sv in self.DFSTopologicalSortVertex(v, visited): yield sv
        else:
            for v in self.__adjacencyMatrix.AllVertexes():
                if v in visited: continue
                for sv in self.DFSTopologicalSortVertex(v, visited): yield sv

    def BFSTopologicalSortVertex(self, v, visited = None):
        if v is None: raise Exception("input None vertex")
        if not self.__adjacencyMatrix.CheckVertexExist(v):
            raise Exception("node not exist in graph")
        if visited is None: visited = set()
        queue = Queue()
        queue.Enqueue(v)
        visited.add(v)
        while len(queue) > 0:
            v, _ = queue.Dequeue()
            for av, _ in self.__adjacencyMatrix.AllSuccessors(v):
                if av in visited: continue
                visited.add(av)
                queue.Enqueue(av)
            yield v

    def BFSTopologicalSortAll(self):
        visited = set()
        if self.__adjacencyMatrix.IsDigraph():
            for v in self.__adjacencyMatrix.ZeroInDegreeVertexes():
                if v in visited: continue
                for sv in self.BFSTopologicalSortVertex(v, visited): yield sv
        else:
            for v in self.__adjacencyMatrix.AllVertexes():
                if v in visited: continue
                for sv in self.BFSTopologicalSortVertex(v, visited): yield sv
