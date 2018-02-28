'''
Created on 06-Jan-2018

@author: rjoshi
'''

def maxSum1(nums):
    maxSoFar = maxTillNow = int(nums[0])
    for i in range(1, len(nums)):
        maxTillNow = max(int(nums[i]), maxTillNow + int(nums[i]))
        maxSoFar = max(maxTillNow, maxSoFar)
    return maxSoFar

def maxSum2(nums):
    maxSoFar = 0
    maxTillNow = 0
    for i in range(0, len(nums)):
        maxTillNow = maxTillNow + int(nums[i])
        maxSoFar = max(maxTillNow, maxSoFar)
        if maxTillNow < 0:
            maxTillNow = 0
    return maxSoFar

def getLR(nums):
    n = len(nums)
    tsum = 0
    
    lsum = 0
    lidx = n - 1
    for l in range(lidx, -1, -1):
        tsum += int(nums[l])
        if tsum > lsum:
            lsum = tsum
            lidx = l
    
    rsum = 0
    ridx = 0
    for r in range(0, n):
        tsum += int(nums[r])
        if tsum > rsum:
            ridx = r
            rsum = tsum
            
    return (lsum+rsum, (lidx, ridx))
    
    
    

tests = int(input())
res = []
for x in range(0, tests):
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    
    nums = input().split(" ")
    n = len(nums)
    msum = 0
    isNeg = 0
    for i in range(0, n):
        msum += int(nums[i])
        if int(nums[i]) < 0 and isNeg == 0:
            isNeg = 1
    
#     tnums = []
#     for v in range(0, k):
#         tnums += nums
#     res.append(maxSum(tnums))
    
    if isNeg == 0:
        res.append(msum*k)
    elif msum >= 0:
        fsum = maxSum1(nums)
        if k == 1:
            res.append(fsum)
        else:
            fsum2 = maxSum1(nums+nums)
            res.append(fsum2 + (k-2)*msum)
    else:
        fsum = maxSum1(nums)
        if k == 1:
            res.append(fsum)
        else:
            sum1 = maxSum1(nums+nums)
            res.append(max(fsum, sum1))
        
for xx in res:
    print(xx)