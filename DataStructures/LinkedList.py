class LLNode(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class LinkedList(object):
    def__init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        result = "# "
        for node in self.IterateForward():
            result += node.key + " -> "
        result += '#'
        return result

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
        tailNone.prev = None
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
            for node in IterateForward():
                if node.key == key: return node
        else:
            for node in IterateBackward():
                if node.key == key: return node
        return None




