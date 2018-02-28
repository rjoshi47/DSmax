'''
Created on 08-Oct-2017

@author: rjoshi
'''
def getMaxContiguousProduct(arr):
    maxMulSoFar = 1
    maxMulTillNow = 1
    
    for i in range(0, len(arr)):
        maxMulTillNow *= arr[i]
        if maxMulSoFar < maxMulTillNow:
            maxMulSoFar = maxMulTillNow
        
        if maxMulTillNow == 0:
            maxMulTillNow = 1
    
    print(maxMulSoFar)
    
arr = [-2, -3, 0, -2, -40]
getMaxContiguousProduct(arr)