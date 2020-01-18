import math

class  MaximumSubArray():
    def __call__(self, array):
        return self.__maximumSubArray(array, 0, len(array))

    def __maxCrossingSubArray(self, array, low, mid, high):
        if low < 0 or high > len(array) or mid < low or mid > high:
            raise Exception("Invalide low - mid - high input")
        leftSum = - math.inf
        _sum = 0
        maxLeft = mid - 1
        for i in range(mid - 1, low - 1, -1):
            _sum += array[i]
            if _sum > leftSum:
                leftSum = _sum
                maxLeft = i
        rightSum = - math.inf
        _sum = 0
        maxRight = mid
        for i in range(mid, high):
            _sum += array[i]
            if _sum > rightSum:
                rightSum = _sum
                maxRight = i + 1
        return (maxLeft, maxRight, leftSum + rightSum)

    def __maximumSubArray(self, array, low, high):
        if high == low or low + 1 == high: return (low, high, array[low])
        mid = int((low + high) / 2)
        leftLow, leftHigh, leftSum = self.__maximumSubArray(array, low, mid)
        rightLow, rightHigh, rightSum = self.__maximumSubArray(array, mid, high)
        crossLow, crossHigh, crossSum = self.__maxCrossingSubArray(array, low, mid, high)
        if leftSum > rightSum:
            if leftSum > crossSum: return (leftLow, leftHigh, leftSum)
        else:
            if rightSum > crossSum: return (rightLow, rightHigh, rightSum)
        return (crossLow, crossHigh, crossSum)


# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# low, high, _sum = MaximumSubArray()(arr)
# print(arr[low:high])
