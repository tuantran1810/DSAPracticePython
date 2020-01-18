class LLNode(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

    def __lt__(a, b):
        return a.key < b.key

    def __gt__(a, b):
        return a.key > b.key

    def __str__(self):
        return str(self.key)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        result = "# "
        for node in self.IterateForward():
            result += (str(node.key) + " <-> ")
        result += '#\n'
        result += f"CheckInvariant: {self.CheckInvariant()}\n"
        return result

    def PushHeadBatch(self, keys, data = []):
        for i in range(len(keys)):
            if i >= len(data): self.PushHead(keys[i])
            else: self.PushHead(keys[i], data[i])

    def PushTailBatch(self, keys, data = []):
        for i in range(len(keys)):
            if i >= len(data): self.PushTail(keys[i])
            else: self.PushTail(keys[i], data[i])

    def PushHead(self, key, data = None):
        newNode = LLNode(key, data)
        self.length += 1
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def PushTail(self, key, data = None):
        newNode = LLNode(key, data)
        self.length += 1
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def PopHead(self):
        if self.head is None: return None
        self.length -= 1
        nextNode = self.head.next
        headNode = self.head
        if nextNode is None:
            self.tail = None
            self.head = None
            if self.length != 0:
                print(f"Warning: something wrong, linked list empty but length = {self.length}")
                self.length = 0
        else:
            self.head = nextNode
            nextNode.prev = None
        headNode.next = None
        return headNode

    def PopTail(self):
        if self.tail is None: return None
        self.length -= 1
        prevNode = self.tail.prev
        tailNode = self.tail
        if prevNode is None:
            self.tail = None
            self.head = None
            if self.length != 0:
                print(f"Warning: something wrong, linked list empty but length = {self.length}")
                self.length = 0
        else:
            self.tail = prevNode
            prevNode.next = None
        tailNode.prev = None
        return tailNode

    def IterateForward(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def IterateBackward(self):
        node = self.tail
        while node is not None:
            yield node
            node = node.prev

    def FindKey(self, key, fwd = True):
        if fwd:
            for node in self.IterateForward():
                if node.key == key: return node
        else:
            for node in self.IterateBackward():
                if node.key == key: return node
        return None

    def InsertAfter(self, node, key, data = None):
        if node is None: raise Exception("None node input")
        if node is self.tail:
            self.PushTail(key, data)
            return
        self.length += 1
        newNode = LLNode(key, data)
        nextNode = node.next
        newNode.prev = node
        newNode.next = nextNode
        node.next = newNode
        nextNode.prev = newNode

    def InsertBefore(self, node, key, data = None):
        if node is None: raise Exception("None node input")
        if node is self.head:
            self.PushHead(key, data)
            return
        self.length += 1
        newNode = LLNode(key, data)
        prevNode = node.prev
        newNode.prev = prevNode
        newNode.next = node
        node.prev = newNode
        prevNode.next = newNode

    def IncreasementPush(self, key, data = None):
        if self.head == None:
            self.PushHead(key, data)
            return
        for node in self.IterateBackward():
            if key > node.key:
                self.InsertAfter(node, key, data)
                return
        self.PushHead(key, data)

    def DecreasementPush(self, key, data = None):
        if self.head == None:
            self.PushHead(key, data)
            return
        for node in self.IterateForward():
            if key > node.key:
                self.InsertBefore(node, key, data)
                return
        self.PushTail(key, data)

    def RemoveNode(self, node):
        if node is None: raise Exception("input node is None")
        if node is self.head: return self.PopHead()
        elif node is self.tail: return self.PopTail()
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.length -= 1
        node.prev = None
        node.next = None
        return node

    def RemoveNthNode(self, nth):
        node = None
        if nth >= self.length: raise Exception("input out of range")
        if nth == 0: return self.PopHead()
        elif nth == (self.length - 1): return self.PopTail()
        else:
            for i, n in enumerate(self.IterateForward()):
                if i == nth:
                    node = n
                    break
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.length -= 1
        node.prev = None
        node.next = None
        return node

    def RemoveAll(self):
        self.head = None
        self.tail = None
        self.length = 0

    def CheckInvariant(self):
        if self.head is None and self.tail is None and self.length == 0: return True
        if (self.head is None and self.tail is not None) or (self.head is not None and self.tail is None): return False
        n = 0
        for i, _ in enumerate(self.IterateForward()): n = i
        if (n + 1) == self.length: return True
        return False

class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def Enqueue(self, key, data = None):
        self.PushHead(key, data)

    def Dequeue(self):
        if len(self) == 0: return None
        node = self.PopTail()
        if node is None: raise Exception("popped node is None!")
        return (node.key, node.data)

class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def Push(self, key, data = None):
        self.PushHead(key, data)

    def Pop(self):
        if len(self) == 0: return None
        node = self.PopHead()
        if node is None: raise Exception("popped node is None!")
        return (node.key, node.data)
