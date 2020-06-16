class Entry(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data

    def __gt__(a, b):
        return a.key > b.key

    def __lt__(a, b):
        return a.key < b.key

    def __ge__(a, b):
        return a.key >= b.key

    def __le__(a, b):
        return a.key <= b.key

    def __eq__(a, b):
        return a.key == b.key

    def __str__(self):
        return '[' + str(self.key) + ':' + str(self.data) + ']'

class Heap(object):
    def __init__(self, array = None, maxHeap = True):
        self.__array = [ None ]
        self.__maxHeap = maxHeap
        if array is not None:
            self.__array.extend(array)
            self.__heapify()

    def __parent(self, i):
        if i < 1: return -1
        idx = int(i / 2)
        if idx < 1 or idx >= len(self.__array): idx = -1
        return idx

    def __left(self, i):
        if i < 1: return -1
        idx = 2 * i
        if idx < 1 or idx >= len(self.__array): idx = -1
        return idx

    def __right(self, i):
        if i < 1: return -1
        idx = 2 * i + 1
        if idx < 1 or idx >= len(self.__array): idx = -1
        return idx

    def __len__(self):
        return len(self.__array) - 1

    def __maxReheapDown(self, idx):
        leftIdx = self.__left(idx)
        rightIdx = self.__right(idx)
        largest = idx
        if leftIdx > 0 and self.__array[leftIdx] > self.__array[idx]: largest = leftIdx
        if rightIdx > 0 and self.__array[rightIdx] > self.__array[largest]: largest = rightIdx
        if largest != idx:
            self.__array[largest], self.__array[idx] = self.__array[idx], self.__array[largest]
            self.__maxReheapDown(largest)

    def __maxReheapUp(self, idx):
        pIdx = self.__parent(idx)
        if pIdx > 0 and self.__array[idx] > self.__array[pIdx]:
            self.__array[pIdx], self.__array[idx] = self.__array[idx], self.__array[pIdx]
            self.__maxReheapUp(pIdx)

    def __minReheapDown(self, idx):
        leftIdx = self.__left(idx)
        rightIdx = self.__right(idx)
        smallest = idx
        if leftIdx > 0 and self.__array[leftIdx] < self.__array[idx]: smallest = leftIdx
        if rightIdx > 0 and self.__array[rightIdx] < self.__array[smallest]: smallest = rightIdx
        if smallest != idx:
            self.__array[smallest], self.__array[idx] = self.__array[idx], self.__array[smallest]
            self.__minReheapDown(smallest)

    def __minReheapUp(self, idx):
        pIdx = self.__parent(idx)
        if pIdx > 0 and self.__array[idx] < self.__array[pIdx]:
            self.__array[pIdx], self.__array[idx] = self.__array[idx], self.__array[pIdx]
            self.__minReheapUp(pIdx)

    def __heapify(self):
        for i in range(int(len(self) / 2), 0, -1):
            if self.__maxHeap:
                self.__maxReheapDown(i)
            else:
                self.__minReheapDown(i)

    def HeadKey(self):
        if len(self) <= 0: return None
        return self.__array[1]

    def PopHead(self):
        if len(self) <= 0: return None
        self.__array[1], self.__array[len(self)] = self.__array[len(self)], self.__array[1]
        data = self.__array.pop()
        if self.__maxHeap: self.__maxReheapDown(1)
        else: self.__minReheapDown(1)
        return data

    def Push(self, value):
        self.__array.append(value)
        if (self.__maxHeap): self.__maxReheapUp(len(self))
        else: self.__minReheapUp(len(self))

    def Iterate(self):
        for i, item in enumerate(self.__array[1:]): yield (i + 1, item)

    def Recheck(self, index):
        if index > len(self.__array) - 1: raise Exception(f"invalid input index = {index}")
        if self.__maxHeap:
            self.__maxReheapUp(index)
            self.__maxReheapDown(index)
        else:
            self.__minReheapUp(index)
            self.__minReheapDown(index)

    def Modify(self, index, new):
        if index > len(self.__array) - 1: raise Exception(f"invalid input index = {index}")
        if new is None: raise Exception("input item is None!")
        self.__array[index] = new
        self.Recheck(index)

    def __str__(self):
        string = "[ "
        for v in self.__array[1:]:
            string += str(v) + ', '
        string += ']'
        return string

class PriorityQueue(object):
    def __init__(self, maxHeap = True):
        self.__heap = Heap(maxHeap = maxHeap)

    def Push(self, key, data = None):
        entry = Entry(key, data)
        self.__heap.Push(entry)

    def Pop(self):
        tmp = self.__heap.PopHead()
        if tmp is not None: return (tmp.key, tmp.data)
        else: return None, None

    def __findDataItem(self, data):
        for idx, item in self.__heap.Iterate():
            if item.data == data: return (idx, item.key, item.data)
        return -1, None, None

    def ModifyKeyOfData(self, data, newKey):
        if data is None: raise Exception("input data is None!")
        idx, oldKey, oldData = self.__findDataItem(data)
        if idx == -1: return
        newItem = Entry(newKey, oldData)
        self.__heap.Modify(idx, newItem)

    def __len__(self):
        return len(self.__heap)

    def __str__(self):
        return str(self.__heap)

