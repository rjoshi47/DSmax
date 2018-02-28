'''
Created on 12-Sep-2017

@author: rjoshi
'''

#nums = [-1, 13, 1, 3, 0, -1, -1, 2, -10, 11, -14, 100]

#nums = [-1, 2, -5, 4, -2, -4, 5,-1, 2, -5, 4, -2, -4, 5,-1, 2, -5, 4, -2, -4, 5]
nums = [-1, 2, -4, 4, -1, 5,-1, 2, -4, 4, -1, 5,-1, 2, -4, 4, -1, 5,-1, 2, -4, 4, -1, 5]
nums = [1, -2, 3, -8, 2, -2, 5,1, -2, 3, -8, 2, -2, 5,1, -2, 3, -8, 2, -2, 5,1, -2, 3, -8, 2, -2, 5]
maxSoFar = maxTillNow = nums[0]
indices = ""
for i in range(1, len(nums)):
    
        
    maxTillNow = max(nums[i], maxTillNow + nums[i])
    
    if nums[i] ==  maxTillNow and nums[i] > maxSoFar:
        indices = " " + str(i) +" "
    elif nums[i] <= maxTillNow and maxTillNow >= maxSoFar:
        indices = " "+ indices + " " + str(i) +" "
    maxSoFar = max(maxTillNow, maxSoFar)

gsum = 0
for i in range(0, len(nums)):
    gsum += nums[i]
print((gsum, maxSoFar))
#print(indices)

def maxSum(nums):
    maxSoFar = 0
    maxTillNow = 0
    for i in range(0, len(nums)):
        maxTillNow = maxTillNow + int(nums[i])
        maxSoFar = max(maxTillNow, maxSoFar)
        if maxTillNow < 0:
            maxTillNow = 0
    return maxSoFar

print(maxSum(nums))