'''
Created on 21-Oct-2017
http://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/
@author: rjoshi
'''

def miniMizeDiff(arr, k):
    arr.sort()
    n = len(arr)
    small = arr[0] + k
    big = arr[n-1] - k
    
    for i in range(1, n):
        numkAdd = arr[i] + k
        numkSub = arr[i] - k
        if numkSub >= small or numkAdd <= big:
            continue
        
        if numkAdd - small <= big - numkSub:
            big = numkAdd
        else:
            small = numkSub
    
    return big - small
    

arr = [15, 5, 1, 10] 
k = 3
print(miniMizeDiff(arr, k))