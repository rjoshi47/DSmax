'''
Created on 16-Oct-2017

@author: rjoshi
'''

def findMaxNonAdjacentElementSum(arr):
    maxSumTillNow1 = maxSumTillNow2 = maxSumSoFar1 = maxSumSoFar2 = 0
    for i in range(0, len(arr)):
        if i%2 == 1:
            maxSumTillNow1 = maxSumTillNow1 + arr[i]
            if maxSumTillNow1 > maxSumSoFar1:
                maxSumSoFar1 = maxSumTillNow1
            if maxSumTillNow1 < 0:
                maxSumTillNow1 = 0
        else:
            maxSumTillNow2 = maxSumTillNow2 + arr[i]
            if maxSumTillNow2 > maxSumSoFar2:
                maxSumSoFar2 = maxSumTillNow2
            if maxSumTillNow2 < 0:
                maxSumTillNow2 = 0
    return max(maxSumSoFar1, maxSumTillNow2)

def maxDiffWithmaxOnrightOfmin(arr):
    minIdx = 0
    maxDiff = arr[1] - arr[0]
    for i in range(0, len(arr)):
        if arr[i] - arr[minIdx] > maxDiff:
            maxDiff = arr[i] - arr[minIdx]
        if arr[i] < arr[minIdx]:
            minIdx = i
    return maxDiff

def maxDiffforJgreaterthanI(arr):
    minTilli = [0]*len(arr)
    maxTillj = [0]*len(arr)
    
    minTilli[0] = arr[0]
    maxTillj[len(maxTillj)-1] = arr[len(arr)-1]
    
    for i in range(1, len(arr)):
        minTilli[i] = min(minTilli[i-1], arr[i])
    
    for j in range(len(arr)-2, -1,-1):
        maxTillj[j] = max(maxTillj[j+1], arr[j])
    
    i = 0
    j = 0
    maxDiff = -1
    while i < len(arr) and j < len(arr):
        if minTilli[i] < maxTillj[j]:
            maxDiff = max(maxDiff, j-i)
            j += 1
        else:
            i += 1
    return maxDiff
    
        
arr= [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
print(maxDiffforJgreaterthanI(arr))

arr = [34, 8, 10, 23, 12, 80, 30, 33, 1]
print(maxDiffWithmaxOnrightOfmin(arr))
    
    
arr= [1, 20, 3]
print(findMaxNonAdjacentElementSum(arr))
















