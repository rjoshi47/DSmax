'''
dp[n][s] = no of ways n digits sum up to s amount
dp[n][s] = dp[n-1][m-x]
Define x:
We know 1 digit can have value from 0 - 9. If we can find all numbers with n-1 digits with sum of digits [m - x] where 0 <= x <= 9.

Example:
1. dp[2][3] = dp[1][3] + dp[1][2] + dp[1][1] # The second digit have value between 0-9
2. dp[3][25] = dp[2][18] + dp[2][17] + dp[2][16]
    Here, dp[2][25] is not possible as we can have max sum 18 with 2 digits. 
    So, we start with dp[2][18] and end with dp[2][16] as last bit can have max value 9 and 16+9 = 25

@author rjoshi
'''
res = []
dp = [[ 0 for x in range(1001)] for y in range (101)]
M = 1000000000 + 7

for n in range(1, 101):
    for s in range(1, 1001):
        if n*9 < s:
            dp[n][s] = -1
            break
        if n == 1:
            if s <= 9:
                dp[n][s] = 1
        else:
            maxValForOneLessBit = 9*(n-1)
            sumInOneBit = 0
            if s - maxValForOneLessBit > 0: # Example 2
                sumInOneBit = s - maxValForOneLessBit
            for x in range(sumInOneBit, 10):
                if s - x > 0:
                    dp[n][s] = (dp[n][s] + dp[n-1][s-x]) % M
                else:
                    break
        
for _ in range(int(input().strip())):
    (r, c) = input().strip().split(" ")
    if dp[int(r)][int(c)] == 0:
        res.append(-1)
    else:
        res.append(dp[int(r)][int(c)])
        
for xx in res:
    print(xx)
