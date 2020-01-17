class BSTNode(object):
    def __init__(self, key, data, p = None):
        self.key = key
        self.data = data
        self.p = p
        self.left = None
        self.right = None

    def __lt__(a, b):
        return a.key < b.key

    def __eq__(a, b):
        return a.key == b.key

    def __ge__(a, b):
        return a.key >= b.key

    def __str__(self):
        return str(self.key)

class BST(object):
    def __init__(self, recursive = True):
        self.root = None
        self.recursiveMode = recursive

    def Insert(self, key, data = None):
        newNode = BSTNode(key, data)
        if self.root is None: self.root = newNode
        else:
            if self.recursiveMode:
                self._insertRecursive(self.root, newNode)
            else:
                self._insertLooping(newNode)

    def InsertBatch(self, keys, data = []):
        for i in range(len(keys)):
            if i < len(data): self.Insert(keys[i], data[i])
            else: self.Insert(keys[i])

    def _insertRecursive(self, rootNode, newNode):
        if newNode < rootNode:
            if rootNode.left is not None: self._insertRecursive(rootNode.left, newNode)
            else:
                newNode.p = rootNode
                rootNode.left = newNode
        else:
            if rootNode.right is not None: self._insertRecursive(rootNode.right, newNode)
            else:
                newNode.p = rootNode
                rootNode.right = newNode

    def _insertLooping(self, newNode):
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

    def InorderTraversal(self):
        buf = []
        self.__inorderTraversal(self.root, buf)
        return buf

    def __inorderTraversal(self, node, buf):
        if node is not None:
            self.__inorderTraversal(node.left, buf)
            buf.append(node.key)
            self.__inorderTraversal(node.right, buf)

    def PreorderTraversal(self):
        buf = []
        self.__preorderTraversal(self.root, buf)
        return buf

    def __preorderTraversal(self, node, buf):
        if node is not None:
            buf.append(node.key)
            self.__preorderTraversal(node.left, buf)
            self.__preorderTraversal(node.right, buf)

    def PostorderTraversal(self):
        buf = []
        self.__postorderTraversal(self.root, buf)
        return buf

    def __postorderTraversal(self, node, buf):
        if node is not None:
            self.__postorderTraversal(node.left, buf)
            self.__postorderTraversal(node.right, buf)
            buf.append(node.key)

    def MinNode(self):
        return self.__treeMin(self.root)

    def __minNode(self, rootNode):
        if rootNode is None: raise Exception("root node is None!")
        while (rootNode.left is not None):
            rootNode = rootNode.left
        return rootNode

    def MaxNode(self):
        return self.__maxNode(self.root)

    def __maxNode(self, rootNode):
        if rootNode is None: raise Exception("root node is None!")
        while (rootNode.right is not None):
            rootNode = rootNode.right
        return rootNode

    def Successor(self, node):
        if node is None: raise Exception("input node is None!")
        if node.right is not None: return self.__minNode(node.right)
        parentNode = node.p
        while parentNode is not None and node is parentNode.right:
            node = parentNode
            parentNode = parentNode.p
        return parentNode

    def Predecessor(self, node):
        if node is None: raise Exception("input node is None!")
        if node.left is not None: return self.__maxNode(node.left)
        parentNode = node.p
        while parentNode is not None and node is parentNode.left:
            node = parentNode
            parentNode = parentNode.p
        return parentNode

    def __transplant(self, u, v): #replace u with v
        if u is None: raise Exception("input node u is None")
        if u.p is None: self.root = v
        elif u.p.left == u: u.p.left = v
        else: u.p.right = v
        if v is not None: v.p = u.p

    def _deleteNode(self, node):
        if node is None: raise Exception("input node is None")
        if node.left is None:
            self.__transplant(node, node.right)
            return node.right
        elif node.right is None:
            self.__transplant(node, node.left)
            return node.left
        else:
            successor = self.__minNode(node.right)
            if successor.p is not node:
                self.__transplant(successor, successor.right)
                successor.right = node.right
                node.right.p = successor
            self.__transplant(node, successor)
            successor.left = node.left
            node.left.p = successor
            return successor

    def Delete(self, key):
        node = self.Find(key)
        if node is not None: self._deleteNode(node)
        return node

    def __invarianceCheck(self, node):
        if node is None: return True
        result = True
        if node.right is not None: result = result and (node.right >= node)
        if node.left is not None: result = result and (node.left < node)
        return result and (self.__invarianceCheck(node.right)) and (self.__invarianceCheck(node.left))

    def InvarianceCheck(self):
        return self.__invarianceCheck(self.root)

    def __treeStringRecursive(self, node, level, side = 'root'):
        if node is None: return ""
        string = self.__treeStringRecursive(node.right, level + 1, 'R')
        string += '-'*6*level + ' ' + str(node) + '(' + side + ')' + '\n'
        string += self.__treeStringRecursive(node.left, level + 1, 'L')
        return string

    def __treeString(self):
        return self.__treeStringRecursive(self.root, 0)

    def __str__(self):
        result = "Inorder travel:\n"
        result += str(self.InorderTraversal()) + '\n'
        result += "Tree:\n"
        result += self.__treeString()
        result += "Invariance check: " + str(self.InvarianceCheck()) +'\n'
        return result
