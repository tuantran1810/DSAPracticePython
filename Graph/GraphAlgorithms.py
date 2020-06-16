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

    def DepthFirstSearchTime(self):
        visited = {}
        result = {}
        result["visitedTime"] = {}
        result["finishedTime"] = {}
        result["distance"] = {}
        result["predecessor"] = {}
        result["edgesType"] = {}
        time = 0
        for v in self.__adjacencyMatrix.AllInorderedVertexes():
            if v not in visited:
                result["distance"][v] = 0
                result["predecessor"][v] = None
                time = self.__depthFirstSearchTimeVisit(v, visited, result, time)
        return result

    def __depthFirstSearchTimeVisit(self, v, visited, result, time):
        time += 1
        result["visitedTime"][v] = time
        visited[v] = 'g'
        for sv, _ in self.__adjacencyMatrix.AllInorderedSuccessors(v):
            if sv not in visited:
                result["predecessor"][sv] = v
                result["distance"][sv] = result["distance"][v] + 1
                result["edgesType"][(v, sv)] = 't'
                time = self.__depthFirstSearchTimeVisit(sv, visited, result, time)
            elif visited[sv] == 'g':
                result["edgesType"][(v, sv)] = 'b'
            else:
                vtime_u = result["visitedTime"][v]
                vtime_sv = result["visitedTime"][sv]
                if vtime_u < vtime_sv: result["edgesType"][(v, sv)] = 'f'
                else: result["edgesType"][(v, sv)] = 'c'
        time += 1
        result["finishedTime"][v] = time
        visited[v] = 'b'
        return time

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
        stack = Stack()
        if self.__adjacencyMatrix.IsDigraph():
            for v in self.__adjacencyMatrix.ZeroInDegreeVertexes():
                if v in visited: continue
                self.__dfsTopoSortVertex(v, visited, stack)
        else:
            raise Exception("this graph is not a digraph")
        while len(stack) > 0:
            v, _ = stack.Pop()
            yield v

    def __bfsTopoSortImp(self, visited, queue):
        while len(queue) > 0:
            v, _ = queue.Dequeue()
            for av, _ in self.__adjacencyMatrix.AllSuccessors(v):
                if av in visited: continue
                visited.add(av)
                queue.Enqueue(av)
            yield v

    def BFSTopologicalSortVertex(self, v, visited = None, queue = None):
        if v is None: raise Exception("input None vertex")
        if not self.__adjacencyMatrix.CheckVertexExist(v):
            raise Exception("node not exist in graph")
        if visited is None: visited = set()
        if queue is None: queue = Queue()
        queue.Enqueue(v)
        visited.add(v)
        for sv in self.__dfsTopoSortImp(visited, queue): yield sv

    def BFSTopologicalSortAll(self):
        visited = set()
        queue = Queue()
        if self.__adjacencyMatrix.IsDigraph():
            for v in self.__adjacencyMatrix.ZeroInDegreeVertexes():
                queue.Enqueue(v)
                visited.add(v)
        else:
            raise Exception("this graph is not a digraph")
        for v in self.__bfsTopoSortImp(visited, queue): yield v
