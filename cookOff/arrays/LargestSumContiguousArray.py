'''
Created on 08-Oct-2017

@author: rjoshi
'''

def getLargestContiguousSum(arr):
    maxSumSoFar = maxSumTillNow = 0
    tsi = si = ei = 0
    for i in range(0, len(arr)):
        xx = arr[i]
        
        maxSumTillNow = maxSumTillNow + xx
        if maxSumSoFar < maxSumTillNow:
            maxSumSoFar = maxSumTillNow
            si = tsi
            ei = i
                
            
        if maxSumTillNow < 0:
            maxSumTillNow = 0
            tsi = i+1
    
    print(maxSumSoFar)
    return (si, ei)

arr = [-1, -1, 12,-4, 6, -3, 4, -3, 3, 1, -1]
print(getLargestContiguousSum(arr))