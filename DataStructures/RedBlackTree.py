import BST

class RedBlackNode(BST.BSTNode):
    def __init__(self, nilNode, key, data, p = None, blackNode = False):
        super().__init__(key, data, p)
        self.isBlack = blackNode
        self.p = nilNode
        self.left = nilNode
        self.right = nilNode

class RedBlackTree():
    def __init__(self):
        self.NilNode = RedBlackNode(None, "Nil", None, None, True)
        self.NilNode.p = self.NilNode
        self.NilNode.left = self.NilNode
        self.NilNode.right = self.NilNode
        self.root = self.NilNode

    def __leftRotate(self, node):
        if node is None: raise Exception("node is None!")
        if node.right is None: raise Exception("right node is None!")
        upNode = node.right
        node.right = upNode.left
        if node.right is not self.NilNode: node.right.p = node
        upNode.p = node.p
        if upNode.p is self.NilNode: self.root = upNode
        elif node is node.p.left: node.p.left = upNode
        else: node.p.right = upNode
        upNode.left = node
        node.p = upNode

    def __rightRotate(self, node):
        if node is None: raise Exception("node is None!")
        if node.left is None: raise Exception("left node is None!")
        upNode = node.left
        node.left = upNode.right
        if node.left is not self.NilNode: node.left.p = node
        upNode.p = node.p
        if upNode.p is self.NilNode: self.root = upNode
        elif node is node.p.left: node.p.left = upNode
        else: node.p.right = upNode
        upNode.right = node
        node.p = upNode

    def __insert(self, root, node):
        if root is None or node is None: raise Exception("root node or input node is None!")
        if node < root:
            if root.left is self.NilNode:
                root.left = node
                node.p = root
            else: self.__insert(root.left, node)
        else:
            if root.right is self.NilNode:
                root.right = node
                node.p = root
            else: self.__insert(root.right, node)

    def InsertBatch(self, keys, data = []):
        for i in range(len(keys)):
            if i < len(data): self.Insert(keys[i], data[i])
            else: self.Insert(keys[i])

    def Insert(self, key, data = None):
        node = RedBlackNode(self.NilNode, key, data)
        if self.root is self.NilNode:
            node.isBlack = True
            self.root = node
        else:
            self.__insert(self.root, node)
            self.__rebalance(node)

    def __rebalance(self, node):
        if node is None: raise Exception("input None node!")
        while not node.p.isBlack:
            if node.p is node.p.p.left:
                rightUncle = node.p.p.right
                if not rightUncle.isBlack:
                    node.p.isBlack = True
                    rightUncle.isBlack = True
                    node.p.p.isBlack = False
                    node = node.p.p
                elif node is node.p.right:
                    node = node.p
                    self.__leftRotate(node)
                elif node is node.p.left:
                    node.p.isBlack = True
                    node.p.p.isBlack = False
                    self.__rightRotate(node.p.p)
            else:
                leftUncle = node.p.p.left
                if not leftUncle.isBlack:
                    node.p.isBlack = True
                    leftUncle.isBlack = True
                    node.p.p.isBlack = False
                    node = node.p.p
                elif node is node.p.left:
                    node = node.p
                    self.__rightRotate(node)
                elif node is node.p.right:
                    node.p.isBlack = True
                    node.p.p.isBlack = False
                    self.__leftRotate(node.p.p)
        self.root.isBlack = True

    def InorderTraversal(self):
        buf = []
        self.__inorderTraversal(self.root, buf)
        return buf

    def __inorderTraversal(self, node, buf):
        if node is None: raise Exception("node is None!")
        if node is not self.NilNode:
            self.__inorderTraversal(node.left, buf)
            buf.append(node.key)
            self.__inorderTraversal(node.right, buf)

    def PreorderTraversal(self):
        buf = []
        self.__preorderTraversal(self.root, buf)
        return buf

    def __preorderTraversal(self, node, buf):
        if node is not None and node is not self.NilNode:
            buf.append(node.key)
            self.__preorderTraversal(node.left, buf)
            self.__preorderTraversal(node.right, buf)

    def PostorderTraversal(self):
        buf = []
        self.__postorderTraversal(self.root, buf)
        return buf

    def __postorderTraversal(self, node, buf):
        if node is not None and node is not self.NilNode:
            self.__postorderTraversal(node.left, buf)
            self.__postorderTraversal(node.right, buf)
            buf.append(node.key)

    def Find(self, key):
        node = self.__findRecursive(self.root, key)
        return node

    def __findRecursive(self, rootNode, key):
        if rootNode is None or rootNode is self.NilNode: return None
        if rootNode.key == key: return rootNode
        elif key >= rootNode.key: return self.__findRecursive(rootNode.right, key)
        else: return self.__findRecursive(rootNode.left, key)

    def MinNode(self):
        return self.__treeMin(self.root)

    def __minNode(self, rootNode):
        if rootNode is None or rootNode is self.NilNode: raise Exception("root node is None!")
        while (rootNode.left is not self.NilNode):
            rootNode = rootNode.left
        return rootNode

    def MaxNode(self):
        return self.__maxNode(self.root)

    def __maxNode(self, rootNode):
        if rootNode is None or rootNode is self.NilNode: raise Exception("root node is None!")
        while (rootNode.right is not None):
            rootNode = rootNode.right
        return rootNode

    def Successor(self, node):
        if node is None or node is self.NilNode: raise Exception("input node is None!")
        if node.right is not self.NilNode: return self.__minNode(node.right)
        parentNode = node.p
        while parentNode is not self.NilNode and node is parentNode.right:
            node = parentNode
            parentNode = parentNode.p
        return parentNode

    def Predecessor(self, node):
        if node is None or node is self.NilNode: raise Exception("input node is None!")
        if node.left is not self.NilNode: return self.__maxNode(node.left)
        parentNode = node.p
        while parentNode is not self.NilNode and node is parentNode.left:
            node = parentNode
            parentNode = parentNode.p
        return parentNode

    def __transplant(self, u, v): #replace u with v
        if u is None or u is self.NilNode: raise Exception("input node u is None")
        if u.p is self.NilNode: self.root = v
        elif u.p.left is u: u.p.left = v
        else: u.p.right = v
        v.p = u.p

    def __deleteRebalance(self, x):
        if x is None: raise Exception(f"input None node! node = {x}")
        comp = x is x.p.left
        while x is not self.root and x.isBlack is True:
            if comp:
                w = x.p.right
                if w.isBlack is False:
                    w.isBlack = True
                    x.p.isBlack = False
                    self.__leftRotate(x.p)
                    w = x.p.right
                if w.left.isBlack and w.right.isBlack:
                    w.isBlack = False
                    x = x.p
                elif w.right.isBlack:
                    w.left.isBlack = True
                    w.isBlack = False
                    self.__rightRotate(w)
                    w = x.p.right
                else:
                    w.isBlack = x.p.isBlack
                    x.p.isBlack = True
                    w.right.isBlack = True
                    self.__leftRotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.isBlack is False:
                    w.isBlack = True
                    x.p.isBlack = False
                    self.__rightRotate(x.p)
                    w = x.p.left
                if w.left.isBlack and w.right.isBlack:
                    w.isBlack = False
                    x = x.p
                elif w.left.isBlack:
                    w.right.isBlack = True
                    w.isBlack = False
                    self.__leftRotate(w)
                    w = x.p.left
                else:
                    w.isBlack = x.p.isBlack
                    x.p.isBlack = True
                    w.left.isBlack = True
                    self.__rightRotate(x.p)
                    x = self.root
        x.isBlack = True

    def __deleteNode(self, z):
        """
        z: deleted node
        y: removed or moved within tree
        x: move into y's original position
        """
        if z is None or z is self.NilNode: raise Exception("input None node")
        y = z
        x = None
        yOrigIsBlack = y.isBlack
        if z.left is self.NilNode:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right is self.NilNode:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.__minNode(z.right)
            yOrigIsBlack = y.isBlack
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.isBlack = z.isBlack

        if yOrigIsBlack: self.__deleteRebalance(x)


    def Delete(self, key):
        node = self.Find(key)
        if node is not None: self.__deleteNode(node)
        return node

    def __blackHeight(self, node):
        if node is None: raise Exception("None node input")
        if node is self.NilNode: return 0
        rightHeight = self.__blackHeight(node.right)
        leftHeight = self.__blackHeight(node.left)
        # if rightHeight != leftHeight: raise Exception(f"wrong height: left = {leftHeight}, right = {rightHeight}, node num = {node.key}")
        return rightHeight + 1 if node.isBlack else rightHeight

    def __invarianceCheck(self, node):
        if node is None: raise Exception("input None node!")
        if node is self.NilNode: return True
        self.__blackHeight(node)
        result = True
        if node.right is not self.NilNode: result = result and (node.right >= node)
        if node.left is not self.NilNode: result = result and (node.left < node)
        if node.isBlack is False:
            result = result and (node.left.isBlack and node.right.isBlack)
        return result and (self.__invarianceCheck(node.right)) and (self.__invarianceCheck(node.left))

    def InvarianceCheck(self):
        return self.__invarianceCheck(self.root)

    def __treeStringRecursive(self, node, level, side = 'root'):
        if node is None: raise Exception("meet None child node!")
        elif node is self.NilNode: return ""
        color = "B" if node.isBlack else "R"
        string = self.__treeStringRecursive(node.right, level + 1, 'R')
        string += '-'*6*level + ' ' + str(node) + '(' + side + ", " + color + ')' + '\n'
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