'''
Created on 09-Oct-2017

@author: rjoshi
'''
import random
def getShuffeledArray(arr):
    for i in range(len(arr)-1, -1, -1):
        x = random.randint(0, i)
        arr[x], arr[i] = arr[i], arr[x]
    return arr

print(getShuffeledArray([1,2,3,4,5]))
        