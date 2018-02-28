'''
Created on 28-Oct-2017
http://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
Using given array indexs to store the count
@author: rjoshi

'''

def freqCount(arr):
    n = len(arr)
    
    i = 0
    while i < n:
        ci = i
        cval = arr[ci]
        
        while cval > 0:
            mi = (cval % (n-1))
            mv = arr[mi]
            arr[ci] = 0
            if mv < 0:
                arr[mi] -= 1
                break
            else:
                cval = mv
                arr[mi] = -1
                
        i += 1
        
    print(arr)
    
arr = [3, 1, 1, 3, 2]
freqCount(arr)