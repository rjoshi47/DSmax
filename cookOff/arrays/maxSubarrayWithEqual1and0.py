'''
Created on 08-Oct-2017

@author: rjoshi
'''
def maxArrayWithZeroSum(arr):
    sumArray = [0]*len(arr)
    sumArray[0] = arr[0]
    for i in range(1, len(arr)):
        sumArray[i] = sumArray[i-1] + arr[i]
        
    print(sumArray)
    
    maxLen = 0
    rangeDict = {}
    for i in range(0, len(sumArray)):
        if sumArray[i] == 0:
            maxLen = max(maxLen, i+1)
        elif sumArray[i] in rangeDict:
            maxLen = max(maxLen, i - rangeDict[sumArray[i]])
        else:
            rangeDict[sumArray[i]] = i
    return maxLen

def maxArrayWithEqualOneZero(arr):
    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr[i] = -1
            
    return maxArrayWithZeroSum(arr)

arr = [0, 0, 1, 1, 0]
print(maxArrayWithEqualOneZero(arr))