'''
Created on 01-May-2018

@author: rjoshi
'''
# Kadane's method to find Max sum with start and end indices
def getMaxSubSum(nums):
    s_temp = 0
    s = 0
    e = 0
    max_so_far = 0
    max_till_now = 0
    
    for k in range(0, len(nums)):
        max_till_now += nums[k]
        if max_till_now <= 0:
            max_till_now = 0
            s_temp = k + 1
        
        if max_till_now > max_so_far:
            max_so_far = max_till_now
            s = s_temp
            e = k
    
    return (max_so_far, (s, e))

'''
Algo:
1. We fix left column of the sub matrix and move right column by one by one.
2. We maintain a column prefix array and find max sum sub array in this prefix sum array.
  2.1. Now the (s, e) indexes of max sum array bound the upper and lower half of max-sum sub matrix
  2.2. Each time we obtain a max overall sum we update sub matrix bounds
3. We repeat 1->2 by fixing left column from (0 -> c) and move right column
'''
def getMaxSumRectangle(matrix, r, c):
    currSum = 0
    maxSum = 0
    lCol = 0
    rCol = 0
    uRow = 0
    lRow = 0
    for l in range(0, c):
        tempCol = [0]*r
        for p in range(l, c):
            for k in range(0, r):
                tempCol[k] += matrix[k][p]
            (currSum, (s, e)) = getMaxSubSum(tempCol)
            if currSum > maxSum:
                maxSum = currSum
                lCol = l
                rCol = p
                uRow = s
                lRow = e
    return ((lCol, uRow), (lRow,rCol))
            
res = []         
for _ in range(0, int(input())):
    (r, c) = input().split(" ")
    r = int(r)
    c = int(c)
    tVals = input().split(" ")
    vals = []
    for k in range(0, len(tVals)):
        if len(tVals[k]) > 0:
            vals.append(int(tVals[k]))
    
    matrix = [[0 for i in range(0, c)] for j in range(0, r)]
    k = 0
    for i in range(0, r):
        for j in range(0, c):
            matrix[i][j] = vals[k]
            k += 1
            
    ((lCol, uRow), (lRow,rCol)) = getMaxSumRectangle(matrix, r, c)
    fsum = 0
    for r in range(uRow, lRow+1):
        for c in range(lCol, rCol+1):
            fsum += matrix[r][c] 
    res.append(fsum)
    
for xx in res:
    print(xx)
