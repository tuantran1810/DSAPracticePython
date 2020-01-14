import sys
sys.path.insert(0, './../../DataStructures/')
sys.path.insert(0, './../DataStructures/')
from Heap import Heap

class SortBase():
    def __init__(self):
        self._compare = lambda a, b, r: a > b if r else a <= b

    def __call__(self, array, compare = None, reverse = False):
        if compare is not None: self._compare = compare
        return self._sort(array, reverse)

    def _sort(self, array, reverse):
        raise Exception("Need to be implemented!")

class QuickSort(SortBase):
    def __init__(self):
        super().__init__()

    def __quickSort(self, array, start, stop, reverse):
        if (stop - start <= 1): return
        pivot = array[stop - 1]
        i = start - 1
        for j in range(start, stop - 1):
            if self._compare(array[j], pivot, reverse):
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[stop - 1] = array[stop - 1], array[i + 1]
        self.__quickSort(array, start, i + 1, reverse)
        self.__quickSort(array, i + 2, stop, reverse)
        return array

    def _sort(self, array, reverse):
        return self.__quickSort(array, 0, len(array), reverse)

class HeapSort(SortBase):
    def __init__(self):
        super().__init__()

    def _sort(self, array, reverse):
        heap = Heap(array, reverse)
        sortedArr = []
        while(heap.HeadKey() is not None):
            sortedArr.append(heap.PopHead())
        return sortedArr
