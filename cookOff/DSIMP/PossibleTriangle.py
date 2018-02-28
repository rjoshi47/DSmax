'''
Created on 25-Oct-2017
http://www.geeksforgeeks.org/find-number-of-triangles-possible/
@author: rjoshi
'''

def getPossibleTriangles(arr):
    n = len(arr)
    pT = 0
    arr.sort()
    for i in range(0, n-2):
        k = i+2
        for j in range(i+1, n):
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1
            pT += k - j - 1
    return pT

arr = [1,3,4]
print(getPossibleTriangles(arr))
        
            