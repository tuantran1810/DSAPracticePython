import math

class ActivitiesSelection(object):
    def __call__(self, startArr, endArr):
        if len(startArr) != len(endArr): raise Exception("invalid input!")
        return self.__select(startArr, endArr)

    def __select(self, startArr, endArr):
        zipped = zip(startArr, endArr)
        sortedArr = sorted(zipped, key = lambda x : x[1])
        result = [sortedArr[0]]
        left = sortedArr[0]
        for item in sortedArr:
            if item[0] < left[1]: continue
            left = item
            result.append(item)
        return result


startArr = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
endArr = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
activities = ActivitiesSelection()(startArr, endArr)
print(activities)

