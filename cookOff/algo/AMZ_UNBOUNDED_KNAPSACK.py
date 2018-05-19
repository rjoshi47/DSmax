'''
Created on 19-May-2018

@author: rjoshi

In unbounded knapsack item quantity is infinite. So, we can choose any number of items any number of times.

              dp[i] # Maximum value that can be achieved using i capacity
dp[i] = max (       
              dp[i-w[j]] + val[j] # Adding jth element value + max value with (i-w[j]) capacity.

Input form:
4 8
vals ->   1 4 5 7
weighs -> 1 3 4 5
'''
res = []

def getMaxValue(n, w, vals, weighs):
    dp = [0]*(w+1)
    
    for i in range(w+1):
        for j in range(n):
            if i >= weighs[j]:
                dp[i] = max(dp[i], dp[i-weighs[j]] + vals[j])
    
    return dp[w]

for _ in range(0, int(input())):
    (n, w) = input().split(" ")
    n = int(n)
    w = int(w)
    
    vals = input().split(" ")
    weighs = input().split(" ")
            
    res.append(getMaxValue(n, w, vals, weighs))
    
for xx in res:
    print(xx)
