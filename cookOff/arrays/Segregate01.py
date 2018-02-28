'''
Created on 08-Oct-2017

@author: rjoshi
'''

def segregate01(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] == 1 and arr[r] == 0:
            arr[l] , arr[r] = arr[r] , arr[l]
            l += 1
            r -= 1
        elif arr[l] == 1 and arr[r] == 1:
            r -= 1
        elif arr[l] == 0 and arr[r] == 0:
            l += 1
        else:
            l += 1
            r -= 1
    return arr

print(segregate01([1,0,0,1,1,0,1,0,1,0,1,0,1,0,1]))