'''
Created on 08-Oct-2017

@author: rjoshi

arr =    [4,  6,  3, -9, -5, 1, 3, 0, 2]

sumArr = [4, 10, 13, 4, -1, 0, 3, 3, 5]
'''

def getMaxZeroSumArray(arr):
    sumArr = [0]*len(arr)
    sumArr[0] = arr[0]
    for i in range(1, len(arr)):
        sumArr[i] = sumArr[i-1] + arr[i]
    
    maxSize = 0
    rangeDict = {}
    print(sumArr)
    for i in range(0, len(sumArr)):
        if sumArr[i] == 0:
            maxSize = max(maxSize, i+1)
        elif sumArr[i] in rangeDict:
            maxSize = max(maxSize, i - rangeDict[sumArr[i]])
        else:
            rangeDict[sumArr[i]] = i
    return maxSize
    
arr = [4,  3,  3, -9, -5, 1, 3, 0, 2]
print(getMaxZeroSumArray(arr))