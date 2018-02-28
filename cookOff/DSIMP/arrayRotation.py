'''
Created on 03-Oct-2017

@author: rjoshi
'''
arr = [1,2,3,4,5,6,7,80,90,100,110]

def reverse(arr, l, r):
    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l+=1
        r-=1

def leftRotate(arr, n):
    reverse(arr, 0, n-1)
    reverse(arr, n, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    
def rightRotate(arr, n):
    reverse(arr, 0, len(arr)-1)
    reverse(arr, n, len(arr)-1)
    reverse(arr, 0, n-1)
    
    
   
rightRotate(arr, 4)
print(arr)

    
    