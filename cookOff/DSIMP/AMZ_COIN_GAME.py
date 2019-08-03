'''
Created on Apr 27, 2018

@author: devuser
https://practice.geeksforgeeks.org/problems/max-possible-amount/0

Given a row of n coins of values v1 , v2 ... vn, where n is even. We play a game against an opponent by alternating turns. 
In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, 
and receives the value of the coin. 
Determine the maximum possible amount of money we can definitely win if we move first.


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
for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = list(map(int, input().strip().split(" ")))
        
    p = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        k = i
        for j in range(n - i):
            ip1jm1 = p[j + 1][k - 1] if j + 1 <= k - 1 else 0
            ip2j = p[j + 2][k] if j + 2 <= k else 0
            ijm2 = p[j][k - 2] if j <= k - 2 else 0
            
            p[j][k] = max(nums[j] + min(ip1jm1, ip2j), nums[k] + min(ip1jm1, ijm2))
            k += 1
    res.append(p[0][n-1])
    
for xx in res:
    print(xx)
