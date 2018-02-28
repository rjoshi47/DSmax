'''
Created on 25-Oct-2017

@author: rjoshi
'''

def findPeakUtil(arr, l, r):
    mid = int((l+r)/2)
    if mid == l:
        if mid + 1 <= r: 
            if arr[mid] > arr[mid+1]:
                return arr[mid]
            else:
                return -1
        else:
            return arr[mid] 
    elif mid == r:
        if mid - 1 >= l:
            if arr[mid] > arr[mid-1]:
                return arr[mid]
            else:
                return -1
        else:
            return arr[mid]
    elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    elif arr[mid] < arr[mid-1]:
        return findPeakUtil(arr, l, mid)
    elif arr[mid] < arr[mid+1]:
        return findPeakUtil(arr, mid+1, r)
        
            
    
def findPeak(arr):
    return findPeakUtil(arr, 0, len(arr)-1)

arr=[1, 2, 2, 4, 4, 2]
print(findPeak(arr))