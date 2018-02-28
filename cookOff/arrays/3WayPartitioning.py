'''
Created on 07-Oct-2017

@author: rjoshi

sort an array between range:
 ---> 9 >-----< 12 <---
'''

def threeWayPartition(arr, low, high):
    start = 0
    i = 0
    end = len(arr) - 1
    while i < end:
        if arr[i] < low:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        elif arr[i] > high:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    print(arr)
    
arr = [1, 10, 2, 3, 9, 17, 18, 7, 8, 12 ,4 ,11]
threeWayPartition(arr, 4, 12)
