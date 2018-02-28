'''
Created on 24-Oct-2017
http://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
@author: rjoshi
'''

def subArrayGivenSum(arr, rSum):
    n = len(arr)
    sumMap = {}
    tSum = 0
    for i in range(0, n):
        tSum += arr[i]
        if tSum == rSum:
            return (0, i)
        elif rSum - tSum in sumMap:
            return (sumMap[rSum - tSum], i)
        else:
            sumMap[tSum] = i
            
arr = [1, 4, 20, 3, 10, 5]
print(subArrayGivenSum(arr, 25))