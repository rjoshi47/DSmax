'''
Created on 14-Oct-2017

@author: rjoshi
'''

def zigZag(arr):
    for i in range(1, len(arr)):
        if i%2 == 1 and arr[i] < arr[i-1]:
            arr[i] , arr[i-1] = arr[i-1] , arr[i]
        elif i%2 == 0 and arr[i] > arr[i-1]:
            arr[i] , arr[i-1] = arr[i-1] , arr[i]
            
arr = [6, 5, 4, 3 , 2, 1]
zigZag(arr)
print(arr)