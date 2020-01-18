class AdjacencyMatrix(object):
    def __init__(self, verticesList = None, digraph = False):
        self.__digraph = digraph
        self.__map = {}
        if verticesList is not None:
            for v in verticesList:
                self.__map[v] = {}
                for _v in verticesList:
                    self.__map[v][_v] = None

    def AddNewNode(self, node):
        if node in self.__map: return
        self.__map[node] = {}
        for v in self.__map.keys():
            self.__map[v][node] = None
            self.__map[node][v] = None

    def AddPath(self, startNode, endNode, value = 1):
        if startNode is None or endNode is None: raise Exception("input None node")
        if value is None: raise Exception("input None value")
        if startNode not in self.__map: self.AddNewNode(startNode)
        if endNode not in self.__map: self.AddNewNode(endNode)
        self.__map[startNode][endNode] = value
        if not self.__digraph: self.__map[endNode][startNode] = value

    def GetPath(self, startNode, endNode):
        if startNode is None or endNode is None: raise Exception("input None node")
        if startNode not in self.__map: raise Exception("cannot found start node in map")
        if endNode not in self.__map[startNode]: raise Exception("cannot found end node in map")
        return self.__map[startNode][endNode]

    def DeletePath(self, startNode, endNode):
        if startNode is None or endNode is None: raise Exception("input None node")
        if startNode not in self.__map: raise Exception("cannot found start node in map")
        if endNode not in self.__map[startNode]: raise Exception("cannot found end node in map")
        self.__map[startNode][endNode] = None
        if not self.__digraph: self.__map[endNode][startNode] = None

    def AllSuccessors(self, v):
        if v is None: raise Exception("input None vertex")
        if v not in self.__map: raise Exception("input vertex not in graph")
        adj = self.__map[v]
        for k in adj.keys():
            if adj[k] is not None: yield (k, adj[k])

    def AllPredecessor(self, v):
        if v is None: raise Exception("input None vertex")
        if v not in self.__map: raise Exception("input vertex not in graph")
        keys = self.VertexSet()
        for k in keys:
            if self.__map[k][v] is not None: yield (k, self.__map[k][v])

    def VertexSet(self):
        return self.__map.keys()

    def CheckVertexExist(self, v):
        if v is None: raise Exception("input None vertex")
        return v in self.__map

    def __str__(self):
        keys = sorted(self.__map.keys())
        result = "vertices: " + str(keys) + '\n' + "Matrix: " + '\n'
        for kstart in keys:
            for kend in keys:
                result += "{:<10}".format(str(self.__map[kstart][kend])) + ' '
            result += '\n'
        return result
