'''
Created on Apr 27, 2018

@author: devuser
https://practice.geeksforgeeks.org/problems/max-possible-amount/0
DP with f: sub problem of picking max value with [i, j] coins

              vi + min(f(i+2,j), f(i+1, j-1)) if p1 choose ith coin then p2 will make sure that p1 will get 
f(i,j) = max{                                 min of [i+2, j] if p2 choose i+1 th coin or [i+1,j-1] if p2 choose jth coin.
              vj + min(f(i+1, j-1), f(i, j-2))
f(i,j) = max(num[i], num[j]) if j-i = 1
f(i,j) = num[i] if i==j
'''
res = []
'''
Fill matrix in 
(0,0) (0,1) (0,2) (0,3) 
      (1,1) (1,2) (1,3)
            (2,2) (2,3)
                  (3,3)
Diagonal form
(0,0) 
      (1,1) 
            (2,2) 
                  (3,3)
(0,1) 
      (1,2) 
            (2,3)
(0,2)
      (1,3)

(0,3)
'''
def getMaxPick(maxPicks, nums):
    n = len(nums)
    for k in range(0, n):
        i = 0
        j = k
        while j < n:
            fi2j = maxPicks[i+2][j] if i+2 <= j else 0
            fi1jm1 = maxPicks[i+1][j-1] if i+1 <= j-1 else 0
            fijm2 = maxPicks[i][j-2] if i <= j-2 else 0
            
            picki = nums[i] + min(fi2j, fi1jm1)
            pickj = nums[j] + min(fijm2, fi1jm1)
            
            maxPicks[i][j] = max(picki, pickj)
            
            j += 1
            i += 1
            
    return maxPicks[0][n-1]

for _ in range(0, int(input())):
    n = input()
    inums = input().split(" ")
    nums = []
    for k in range(0, len(inums)):
        if len(inums[k]) > 0:
            nums.append(int(inums[k]))
    n = len(nums)
    maxPicks = [[0 for j in range(0, n)] for i in range(0, n)]
    #print(maxPicks)
    l = 0
    r = len(nums) - 1
    res.append(getMaxPick(maxPicks, nums))
    
for xx in res:
    print(xx)
    
