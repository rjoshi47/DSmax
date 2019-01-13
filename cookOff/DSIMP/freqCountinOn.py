'''
Created on 28-Oct-2017
http://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
Using given array indexs to store the count
@author: rjoshi

'''

def findCounts(arr, n): 
      
    # Traverse all array elements 
    i = 0
    while i<n: 
        if arr[i] <= 0: 
            i += 1
            continue
        elementIndex = arr[i] - 1
        if arr[elementIndex] > 0: 
            arr[i] = arr[elementIndex] 
            arr[elementIndex] = -1   
        else: 
            arr[elementIndex] -= 1
            arr[i] = 0
            i += 1
  
    print ("Below are counts of all elements") 
    for i in range(0,n): 
        print ("%d -> %d"%(i+1, abs(arr[i]))) 
    print ("") 
    
arr = [3, 1, 1, 3, 2]
freqCount(arr)
