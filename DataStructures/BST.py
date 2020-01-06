class BSTNode():
    def __init__(key, data, p = None):
        self.key = key
        self.data = data
        self.p = p
        self.left = None
        self.right = None

    def __lt__(a, b):
        return a.key < b.key

    def __eq__(a, b):
        return a.key == b.key

class BST():
    def __init__(recursive = True):
        self.root = None
        self.recursiveMode = recursive

    def Insert(self, key, data = None):
        newNode = BSTNode(key, data)
        if self.root is None: self.root = newNode
        else:
            if self.recursiveMode:
                self.__insertRecursive(self.root, newNode)
            else:
                self.__insertLooping(newNode)

    def __insertRecursive(self, rootNode, newNode):
        if newNode < rootNode:
            if rootNode.left is not None: self.__insertRecursive(rootNode.left, newNode)
            else:
                newNode.p = rootNode
                rootNode.left = newNode
        else:
            if rootNode.right is not None: self.__insertRecursive(rootNode.right, newNode)
            else:
                newNode.p = rootNode
                rootNode.right = newNode

    def __insertLooping(self, newNode):
        pNode = None
        rootNode = self.root
        while (rootNode is not None):
            pNode = rootNode
            if newNode < rootNode: rootNode = rootNode.left
            else: rootNode = rootNode.right
        newNode.p = pNode
        if pNode is None: self.root = newNode
        elif newNode < pNone: pNode.left = newNode
        else: pNode.right = newNode

    def Find(self, key):
        if self.recursiveMode: return self.__findRecursive(self.root, key)
        else: return self.__findLooping(key)

    def __findRecursive(self, rootNode, key):
        if rootNode is None: return None
        if rootNode.key == key: return rootNode
        elif key >= rootNode.key: return self.__findRecursive(rootNode.right, key)
        else: return self.__findRecursive(rootNode.left, key)

    def __findLooping(self, key):
        node = self.root
        while (node is not None):
            if key == node.key: return node
            elif key >= rootNode.key: node = node.right
            else: node = node.left
        return None

    def InorderTravel(self):
        buf = []
        self.__inorderTravel(self.root, buf)
        return buf

    def __inorderTravel(self, node, buf):
        if node is not None:
            self.__inorderTravel(node.left, buf)
            buf.append(node.key)
            self.__inorderTravel(node.right, buf)

    def MinNode(self):
        return self.__treeMin(self.root)

    def __minNode(self, rootNode):
        if rootNode is None: raise Exception("root node is None!")
        while (rootNode.left is not None):
            rootNode = rootNode.left
        return rootNode

    def MaxNode(self):
        return self.__treeMax(self.root)

    def.__maxNode(self, rootNode):
        if rootNode is None: raise Exception("root node is None!")
        while (rootNode.right is not None):
            rootNode = rootNode.right
        return rootNode

