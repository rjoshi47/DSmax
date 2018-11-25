'''
No of ways to get sum x with dice of m faces in n throws.
Let the input is sum(6,3,8)
DP:

We know in one roll we can get sum from 1 -> 6.
So, no. of. ways to get 7 in 2 rolls = summation of sum(1,7-k) for 1 <= k <= min(m i.e no of faces, 7)
sum(2,7) = sum(1,6) + sum(1,5) + ... + sum(1,1)
similary:
sum(3,9) = sum(2,8) + sum(2,7) + ... + sum(2,3) loop ends at m=6

return sum[3][8]

'''
res = []

def getCombinations(m, n, x):
    sumMat = [[0 for c in range(0,x+1)] for r in range(0, n+1)]

    for j in range(1, min(m,x)+1):
        sumMat[1][j] = 1
    
    for i in range(1, n+1):
        for j in range(1, x+1):
            for k in range(1, min(m,j)+1):
                    sumMat[i][j] += sumMat[i-1][j-k]
                    '''
                    for m = 6
                    dp[2][10] = dp[1][6] + dp[1][5] + dp[1][4] here, k can go max 6 and hence stops at 4 [10-6] or [j-k]
                    '''
            
    return sumMat[n][x]
    
for _ in range(0, int(input())):
    nums = input().strip().split(" ")    
    res.append(getCombinations(int(nums[0]), int(nums[1]), int(nums[2])))
                
for xx in res:
    print(xx)
