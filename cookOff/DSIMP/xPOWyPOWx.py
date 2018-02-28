'''
Created on 26-Oct-2017
http://www.geeksforgeeks.org/find-number-pairs-xy-yx/
@author: rjoshi
'''

def getPairsUtil(num, arr2, l, r):
    mid = int((l+r)/2)
    if mid == r:
        if arr2[mid] > num:
            return (num, arr2[mid])
        else:
            return -1
    elif mid == l:
        if arr2[mid] > num:
            return (num, arr2[mid])
        elif mid+1<=r and arr2[mid+1] > num:
            return (num, arr2[mid+1])
        else:
            return -1
    elif arr2[mid] > num and arr2[mid-1] < num:
            return (num, arr2[mid])
    elif arr2[mid] < num and arr2[mid+1] > num:
            return (num, arr2[mid+1])
    else:
        return getPairsUtil(num, arr2, mid, r)
        
def getPairs(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    arr1.sort()
    arr2.sort()
    pairs = []
    for i in range(0, n):
        pairs.append(getPairsUtil(arr1[i], arr2, 0, m-1))
        
    for i in range(0, m):
        pairs.append(getPairsUtil(arr2[i], arr1, 0, n-1))
        
    print(pairs)
    
    
arr1 = [2, 1, 6]
arr2 = [1, 5]
getPairs(arr1, arr2)