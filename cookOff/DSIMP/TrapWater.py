'''
Created on 29-Oct-2017
http://www.geeksforgeeks.org/trapping-rain-water/
@author: rjoshi
'''

def getTrappedWater(arr):
    n = len(arr)
    maxNextWall = [0]*n
    
    maxNextWall[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] < maxNextWall[i+1]:
            maxNextWall[i] = maxNextWall[i+1]
        else:
            maxNextWall[i] = arr[i]
    
    print(maxNextWall)
    
    water = 0
    maxWallToLeft = arr[0]
    for i in range(1, n-1):
        if arr[i] > maxWallToLeft:
            maxWallToLeft = arr[i]
        else:
            if arr[i] < maxNextWall[i]:
                water = water + min(maxWallToLeft,maxNextWall[i]) - arr[i]
    print(water)
              
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
getTrappedWater(arr) 
            