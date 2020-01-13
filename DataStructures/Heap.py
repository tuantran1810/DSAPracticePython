class Entry(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data

    def __gt__(a, b):
        return a.key > b.key

    def __lt__(a, b):
        return a.key < b.key

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
        leftIdx = __left(idx)
        rightIdx = __right(idx)
        largest = idx
        if leftIdx > 0 and self.__array[leftIdx] > self.__array[idx]: largest = leftIdx
        if rightIdx > 0 and self.__array[rightIdx] > self.__array[idx]: largest = rightIdx
        if largest != idx:
            self.__array[largest], self.__array[idx] = self.__array[idx], self.__array[largest]
            self.__maxHeapify(largest)

    def __maxReheapUp(self, idx):
        pIdx = self.__parent(idx)
        if pIdx > 0 and self.__array[idx] > self.__array[pIdx]:
            self.__array[pIdx], self.__array[idx] = self.__array[idx], self.__array[pIdx]
            self.__maxReheapUp(pIdx)

    def __minReheapDown(self, idx):
        leftIdx = __left(idx)
        rightIdx = __right(idx)
        smallest = idx
        if leftIdx > 0 and self.__array[leftIdx] < self.__array[idx]: smallest = leftIdx
        if rightIdx > 0 and self.__array[rightIdx] < self.__array[idx]: smallest = rightIdx
        if smallest != idx:
            self.__array[smallest], self.__array[idx] = self.__array[idx], self.__array[smallest]
            self.__minHeapify(smallest)

    def __minReheapUp(self, idx):
        pIdx = self.__parent(idx)
        if pIdx > 0 and self.__array[idx] < self.__array[pIdx]:
            self.__array[pIdx], self.__array[idx] = self.__array[idx], self.__array[pIdx]
            self.__maxReheapUp(pIdx)

    def __heapify(self):
        for i in range(len(self) / 2, 0, -1):
            if self.maxHeap:
                self.__maxReheapDown(i)
            else:
                self.__minReheapDown(i)

    def HeadKey(self):
        if len(self) <= 0: return None
        return self.__array[1].key

    def PopHead(self):
        if len(self) <= 0: return None
        self.__array[1], self.__array[len(self)] = self.__array[len(self)], self.__array[1]
        data = self.__array.pop()
        if self.maxHeap: self.__maxReheapDown(1)
        else: self.__minReheapDown(1)
        return data

