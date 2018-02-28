'''
Created on 20-Oct-2017

@author: rjoshi
'''

rangeSum = {}
def preProcess(arr):
    n = len(arr)
    sqrtN = int(n**(1/2))
    parts = sqrtN
    if parts*parts < n:
        parts += 1
    
    for i in range(0, parts):
        j = i*sqrtN
        tSum = 0
        while j < n and j < i*sqrtN + sqrtN:
            tSum += arr[j]
            j += 1
        rangeSum[(i*sqrtN, j-1)] = tSum
    print(rangeSum)    
    
def summ(arr, l , r):
    ss = 0
    for i in range(l,r+1):
        ss += arr[i]
    return ss

def getRangeSum(arr, l, r):
    n = len(arr)
    sqrtN = int(n**(1/2))
    if l < 0 or r >= n:
        return -1
    
    rSum = 0
    while l % sqrtN != 0:
        rSum += arr[l] 
        l += 1
    
    while r % sqrtN  != sqrtN - 1:
        rSum += arr[r] 
        r -= 1

    while l <= r:
        rSum += rangeSum[(l, min(l+sqrtN-1, n-1))]
        l += sqrtN
    
    return rSum

arr = [1,2,3,4,5,6,7,8,9,10,11]
preProcess(arr)
print(getRangeSum(arr, 1, 7))
print(summ(arr, 1, 7))
    
    