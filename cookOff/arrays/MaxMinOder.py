'''
Created on 08-Oct-2017

@author: rjoshi
array need to be sorted to do this 
'''
def reverse(arr, l, r):
    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l+=1
        r-=1
        
def getMaxMinForm(arr):
    for i in range(0, len(arr)):
        reverse(arr, i, len(arr)-1)
        print(arr)
    return arr

print(getMaxMinForm([1, 2, 3, 4, 5, 6, 7]))
    