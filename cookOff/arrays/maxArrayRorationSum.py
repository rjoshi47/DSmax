'''
Created on 04-Oct-2017

 8*0 3*1 1*2 2*3 = 0+3+2+6 = 11
-8*1 3*1 1*1 2*1
+8*4

 8*3 3*0 1*1 2*2
-8*1 3*1 1*1 2*1
+    3*4

8*1 3*2 1*3 2*0 = 9+6+1+0 = 16

8*2 3*3 1*0 2*1 = 16+9+0+2 = 27

8*3 3*0 1*1 2*2 = 24+0+1+4 = 29

@author: rjoshi
'''
arr = [2, 8, 3, 1]

def getMaxRotateSum(arr):
    arrSum = 0
    for num in arr:
        arrSum += num
    
    mSum = 0
    for i in range(0, len(arr)):
        mSum += i*arr[i]
        
    maxSum = mSum
    for i in range(1, len(arr)):
        nxtSum = mSum - arrSum + arr[i-1]*len(arr)
        mSum = nxtSum
        maxSum = max(mSum, maxSum)
    
    return maxSum

print(getMaxRotateSum(arr))
        
        