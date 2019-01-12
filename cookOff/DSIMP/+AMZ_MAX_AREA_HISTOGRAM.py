'''
1
7
6 2 5 4 5 1 6

We have to find the max rectangular area in a hostogram. For above example its the region (5,4,5) where rectangle 
of area 12 (4,4,4) is maximum.

So, the idea here is to find smaller numbers on left and right and them multiplying 
the value with the distance of max min indexes.

Like for i = 3 val = 4 its 4*(5-1-1) where:
min on right i = 5 val = 1
min on left i = 1 val = 2

1
6
1 2 3 4 5 6

If a number has no right min or left min then we have to include all elements on left or right respectivly.
like for i=3 val = 4 area = 4*(all elements on right) = 4*3 = 12

Created on May 8, 2018
@author: rjoshi
'''    

res = []
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().strip().split(" ")))
    
    tStack = [0]
    maxAreaSoFar = nums[0]
    maxAreaTillNow = nums[0]
    k = 1
    
    while k < n or len(tStack) != 0:
        if k < n and (len(tStack) == 0 or nums[tStack[len(tStack)-1]] <= nums[k]):
            tStack.append(k)
            k += 1
        else:
            topi = tStack.pop(len(tStack)-1)
            maxAreaTillNow = int(nums[topi])
            if len(tStack) == 0:
                maxAreaTillNow = maxAreaTillNow*k 
            else: 
                maxAreaTillNow = maxAreaTillNow*(k - tStack[len(tStack)-1] -1)
            maxAreaSoFar = max(maxAreaSoFar, maxAreaTillNow)
    res.append(maxAreaSoFar)
    
for xx in res:
    print(xx)
