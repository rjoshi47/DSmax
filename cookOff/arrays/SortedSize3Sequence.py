'''
Created on 08-Oct-2017

@author: rjoshi

for each index find if it has an element > itself on right of array.
for each index find if it has an element < itself on left of array.

'''
    
def getSortedSize2Seq(arr):
    minELe = ['na']*len(arr)
    maxELe = ['na']*len(arr)
    
    minSoFar = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[minSoFar]:
            minELe[i] = minSoFar
        else:
            minSoFar = i
            
    maxSoFar = len(arr) - 1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[maxSoFar]:
            maxELe[i] = maxSoFar
        else:
            maxSoFar = i
    
    for i in range(0, len(arr)):
        if maxELe[i] != 'na' and minELe[i] != 'na':
            print(arr[minELe[i]], end = " ")
            print(arr[i], end = " ")
            print(arr[maxELe[i]])
            
    
    
    
arr = [9, 12, 11, 10, 5, 6, 2, 30, 6]
getSortedSize2Seq(arr)