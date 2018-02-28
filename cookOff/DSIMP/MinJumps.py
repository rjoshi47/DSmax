'''
Created on 22-Oct-2017
    http://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/ 
@author: rjoshi
'''

def getMinJumps(arr):
    n = len(arr)
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1
    
    for i in range(1, n):
        if i == n-1:
            return jumps
        
        maxReach = max(maxReach, i + arr[i])
        
        steps -= 1
        
        if steps == 0:
            jumps += 1
            # [3, 3, 6, 2, 9, 2, 6, 7, 2, 8, 9]
            # at 2 steps will become 0 and max reach will be ( 2+ 6) = 8
            # and i = 3 but we can still use 5 steps from 2nd 6 value
            # which is maxReach - i = 8 - 3 = 5
            steps = maxReach - i
    return jumps

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(getMinJumps(arr))
    