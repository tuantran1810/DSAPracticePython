class QuickSort():
    def __init__(self):
        self.__compare = lambda a, b, r: a > b if r else a <= b

    def __call__(self, array, compare = None, reverse = False):
        if compare is not None: self.__compare = compare
        self.__quickSort(array, 0, len(array), reverse)
        return array

    def __quickSort(self, array, start, stop, reverse):
        if (stop - start <= 1): return
        pivot = array[stop - 1]
        i = start - 1
        for j in range(start, stop - 1):
            if self.__compare(array[j], pivot, reverse):
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[stop - 1] = array[stop - 1], array[i + 1]
        self.__quickSort(array, start, i + 1, reverse)
        self.__quickSort(array, i + 2, stop, reverse)
