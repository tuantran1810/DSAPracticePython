import sys
sys.path.insert(0, './../DataStructures/')
from Graph import UnweightedIndirectionAdjacencyMatrix
from LinkedList import Queue, Stack
from Heap import PriorityQueue

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

    def MST_Kruskal(self):
        setIndex = {}
        sets = {}
        pq = PriorityQueue(maxHeap = False)
        result = []
        length = 0
        for i, v in enumerate(self.__adjacencyMatrix.AllVertexes()):
            setIndex[v] = i
            sets[i] = set([v])

        for s, e, v in self.__adjacencyMatrix.AllEdges():
            pq.Push(v, (s, e))

        while(len(pq) != 0):
            w, e = pq.Pop()
            start = e[0]
            end = e[1]
            setIndex1 = setIndex[start]
            setIndex2 = setIndex[end]
            if setIndex1 != setIndex2:
                result.append(e)
                length += w
                if setIndex2 > setIndex1:
                    for v in sets[setIndex2]: setIndex[v] = setIndex1
                    sets[setIndex1] = sets[setIndex1].union(sets[setIndex2])
                else:
                    for v in sets[setIndex1]: setIndex[v] = setIndex2
                    sets[setIndex2] = sets[setIndex2].union(sets[setIndex1])
        return (result, length)

    def MST_Prim(self):
        pq = PriorityQueue(maxHeap = False)
        treeVertexes = set()
        result = []
        length = 0
        for v in self.__adjacencyMatrix.AllVertexes():
            pq.Push(0, (v, v))
            break

        while(len(pq) > 0):
            w, v = pq.Pop()
            if v[1] in treeVertexes: continue
            treeVertexes.add(v[1])
            result.append(v)
            length += w
            for s, sw in self.__adjacencyMatrix.AllSuccessors(v[1]):
                if s in treeVertexes: continue
                pq.Push(sw, (v[1], s))
        return (result[1:], length)
