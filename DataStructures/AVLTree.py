import BST

class AVLNode(BST.BSTNode):
    def __init__(self, key, data, p = None):
        super().__init__(key, data, p)
        self.height = 0
        self.lh = -1
        self.rh = -1

    def UpdateHeight(self):
        self.lh = -1 if self.left is None else self.left.height
        self.rh = -1 if self.right is None else self.right.height
        self.height = max(self.lh, self.rh) + 1
        return self.GetBalance()

    def GetBalance(self):
        return self.rh - self.lh

class AVLTree(BST.BST):
    def __init__(self, recursive = True):
        super().__init__(recursive)

    def __leftRotate(self, node):
        if node.right is None: raise Exception("right node is None!")
        upNode = node.right

        node.right = upNode.left
        if node.right is not None: node.right.p = node

        upNode.left = node
        upNode.p = node.p
        if node.p is None: self.root = upNode
        elif node.p.left == node: node.p.left = upNode
        else: node.p.right = upNode
        node.p = upNode
        node.UpdateHeight()
        upNode.UpdateHeight()

    def __rightRotate(self, node):
        if node.left is None: raise Exception("left node is None!")
        upNode = node.left

        node.left = upNode.right
        if node.left is not None: node.left.p = node

        upNode.right = node
        upNode.p = node.p
        if node.p is None: self.root = upNode
        elif node.p.left == node: node.p.left = upNode
        else: node.p.right = upNode
        node.p = upNode
        node.UpdateHeight()
        upNode.UpdateHeight()

    def __rebalance(self, node):
        while node is not None:
            balance = node.UpdateHeight()
            if balance > 2 or balance < -2: raise Exception(f"balance = {balance}")
            if balance == 2:
                rightNode = node.right
                if rightNode is None: raise Exception("balance == 2 but right node is None")
                rBalance = rightNode.GetBalance()
                if rBalance > 1 or rBalance < -1: raise Exception(f"rBalance = {rBalance}")
                if rBalance == 1:
                    self.__leftRotate(node)
                else:
                    self.__rightRotate(rightNode)
                    self.__leftRotate(node)
            if balance == -2:
                leftNode = node.left
                if leftNode is None: raise Exception("balance == 2 but right node is None")
                lBalance = leftNode.GetBalance()
                if lBalance > 1 or lBalance < -1: raise Exception(f"lBalance = {lBalance}")
                if lBalance == -1:
                    self.__rightRotate(node)
                else:
                    self.__leftRotate(leftNode)
                    self.__rightRotate(node)
            node = node.p

    def InsertBatch(self, keys, data = []):
        for i in range(len(keys)):
            if i < len(data): self.Insert(keys[i], data[i])
            else: self.Insert(keys[i])

    def Insert(self, key, data = None):
        newNode = AVLNode(key, data)
        if self.root is None: self.root = newNode
        else:
            if self.recursiveMode: self._insertRecursive(self.root, newNode)
            else: self._insertLooping(newNode)
        self.__rebalance(newNode)

    def Delete(self, key):
        node = super().Delete(key)
        self.__rebalance(node)
        return node
