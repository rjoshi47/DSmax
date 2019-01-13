'''
Created on 12-Dec-2017

@author: rjoshi
'''

def getGivenSum(arr, gsum):
    n = len(arr)
    preSum = arr[0]
    sumDict = {}
    for i in range(1, n):
        preSum += arr[i]
        
        if preSum == gsum:
            return (0, i)
        elif preSum - gsum in sumDict:
            return (sumDict[preSum - gsum]+1, i)
        else:
            sumDict[preSum] = i
    return -1

arr = [5, -2, 10, 2, -2, -20, 10]
print(getGivenSum(arr, -12))
