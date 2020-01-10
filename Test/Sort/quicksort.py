import sys
sys.path.insert(0, './../../Algorithms/')
from sort import QuickSort

arr = [5, 0, 1, 3, 8, 7, 9, 6]
QuickSort()(arr)
print(arr)

arr = [5, 0, 1, 3, 8, 7, 9, 6]
QuickSort()(arr, reverse = True)
print(arr)

