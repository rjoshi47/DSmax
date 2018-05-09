'''
Created on May 8, 2018
https://practice.geeksforgeeks.org/problems/smallest-distant-window/0
@author: rjoshi

1. Init s=0 and start e = 0 and e+= 1 while we have not visited all distinct chars once.
  then s+= 1 while the count of char at s > 1 and decrease its count

2. Now, to check for another unique window
  Remove char at s and decrease its count
  Repeate 1

'''

res = []
for _ in range(int(input())):
    nums = input().strip()
    
    countDict = {}
    s = 0
    
    for e in range(0, len(nums)):
        countDict[nums[e]] = 0
    
    count = 100000
    totalDistinctChars = len(countDict)
    distinctCharsSoFar = 0
    for e in range(0, len(nums)):
        if countDict[nums[e]] == 0:
            distinctCharsSoFar += 1
        countDict[nums[e]] += 1
        
        if distinctCharsSoFar == totalDistinctChars:
            while s < e:
                if countDict[nums[s]] > 1:
                    countDict[nums[s]] -= 1
                    s += 1
                else:
                    break
            
            count = min(count, e-s+1)
            if s+1 < len(nums):
                countDict[nums[s]] -= 1
                s += 1
                distinctCharsSoFar -= 1
            
            
    res.append(count)

for xx in res:
    print(xx)
    
    
    
