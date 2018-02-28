'''
Created on 04-Oct-2017
@author: rjoshi
'''
arr =[80, 90, 100, 110, 120, 2, 3, 4, 5, 6, 7]
def findPiv(arr, l, h):
    if l > h:
        return -1
    if l == h:
        return l
    mid = int((l+h)/2)
    if mid < h and arr[mid] > arr[mid+1]:
        return mid
    elif mid > l and arr[mid] < arr[mid-1]:
        return mid - 1
    elif arr[l] >= arr[mid]:
        return findPiv(arr, l, mid-1)
    else:
        return findPiv(arr, mid+1, h)

def findPairWithSum(arr, psum):
    maxi = findPiv(arr, 0, len(arr)-1)
    mini = maxi + 1
    n = len(arr)
    while maxi != mini:
        if arr[maxi] + arr[mini] == psum:
            return (arr[maxi] , arr[mini])
        elif arr[maxi] + arr[mini] > psum:
            maxi = (n + maxi - 1) % n
        else:
            mini = (mini + 1)%n

print(findPairWithSum(arr, 97))
    
    