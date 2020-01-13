'''
Created on 13-Jan-2020

@author: rjoshi
https://www.geeksforgeeks.org/word-wrap-problem-dp-19/
'''
from math import inf

def word_wrap(nums, k):
    nums = [0] + nums
    n = len(nums)
    dp = [[inf for i in range(n)] for j in range(n)]
    
    for i in range(1, n):
        if k >= nums[i]:
            dp[i][i] = k - nums[i]
    
    for i in range(1, n):
        if k < nums[i]:
            continue
        
        spaces = 1
        tk = k - nums[i]
        for j in range(i + 1, n):
            if (tk - spaces) - nums[j] < 0:
                break
            
            dp[i][j] = tk - nums[j]
            tk -= nums[j]
            spaces += 1
            
    for i in range(0, n):
        print(dp[i])
    
    c = [inf]*n
    c[0] = 0
    c[1] = dp[1][1]**2
    for j in range(2, n):
        for i in range(1, j + 1):
            c[j] = min(c[j], c[i - 1] + dp[i][j]**2)
    
    print(c)
    
word_wrap([3, 2, 2, 5], 6)
    
