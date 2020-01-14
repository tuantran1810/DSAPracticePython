import sys
sys.path.insert(0, './../../DataStructures/')
from LinkedList import LinkedList

class EntryData(object):
    def __init__(self, data, ptr = None):
        self.ptr = ptr
        self.data = data

class EntryLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def __newLinkedListFromNodes(self, node):
        if node is None: raise Exception("input None node")
        ll = EntryLinkedList()
        ll.head = node
        for i, n in enumerate(ll.IterateForward()):
            ll.tail = n
            ll.length = i + 1
        return ll

    def __renewLength(self):
        for i, n in enumerate(self.IterateForward()):
            self.length = i + 1

    def SplitAtNode(self, node):
        left = None
        center = None
        right = None
        if node is self.head:
            self.PopHead()
            center = self.__newLinkedListFromNodes(node)
            right = self
        elif node is self.tail:
            self.PopTail()
            center = self.__newLinkedListFromNodes(node)
            left = self
        else:
            rightNode = node.next
            leftNode = node.prev
            node.next = None
            node.prev = None
            leftNode.next = None
            rightNode.prev = None

            left = self
            left.tail = leftNode
            left.__renewLength()

            center = self.__newLinkedListFromNodes(node)
            right = self.__newLinkedListFromNodes(rightNode)
        return (left, center, right)

class BNode(object):
    def __init__(self, t = 2, parents = None):
        self.t = t
        if t < 2: raise Exception("t is less than 2!")
        self.m = 2*t -1
        self.nKeys = 0
        self.isLeaf = True
        self.firstPtr = None
        self.entries = EntryLinkedList()
        self.parents = parents

    def MergeWith(self, other):
        if other is None: raise Exception("other is None")


    def __insertAndSplit(self, key, data):
        entry = EntryData(data)
        self.entries.IncreasementPush(key, entry)
        centerNode = None
        for i, node in enumerate(self.entries):
            if i == self.t:
                centerNode = node
                break
        if centerNode is None: raise Exception("centerNode entry is None")
        return self.entries.SplitAtNode(centerNode)

    def Insert(self, key, data):
        if self.nKeys >= m: raise Exception("nkeys in node excess m")
        left, center, right = (None, None, None)
        if self.nKeys < (m - 1):
            self.nKeys += 1
            entry = EntryData(data)
            self.entries.IncreasementPush(key, entry)
            center = self
        else:
            left, center, right = self.__insertAndSplit(key, data)
            if left is None or center is None or right is None: raise Exception("left, center or right is None!")
            if len(center) != 1: raise Exception("length of center != 1")
            if len(left) != len(right): raise Exception("length left != length right")
            if len(left) + len(right) + len(center) != self.m: raise Exception("number of entries after splitting not make sense")
        return left, center, right

    def Find(self, key):
        tmp = None
        for node in entries.IterateForward():
            if node.key == key: return node
            elif node.key > key:
                tmp = node
                break
        if
        nextPtr = None
        if tmp.prex is not None:
            nextPtr = tmp.prev.
        return None

class BTree(object):
    def __init__(self, t = 2):
        self.t = t
        self.m = 2*t - 1
        self.root = None

    def __find(self, key, node):
        if node is None: return None
        tmp = node.Find(key)
        if tmp is None:


    def Find(self, key):
        if root is None: return None


    def Insert(self, key, data):
        if self.root is None:
            self.root = BNode()
            self.root.Insert(key, data)
        else:


