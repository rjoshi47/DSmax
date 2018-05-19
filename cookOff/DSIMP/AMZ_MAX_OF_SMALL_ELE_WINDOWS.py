'''
Created on 19-May-2018

for an array of size n print maximum among minimum elements found in winow of size k.
1 <= k <= n

nums = [10 20 30 50 10 70 30]
for k = 2
windows = [10 20] [20 30] [30 50] [50 10] [10 70] [70 30]
min ele = 10 20 30 10 10 30
max ele = 30

We need to find this for k = 1 to 7

@author: rjoshi
'''
res = []

for _ in range(0, int(input())):
    n = int(input())
    tnums = input().split(" ")
    nums = []
    for k in range(0, n):
        if len(tnums[k]) > 0:
            nums.append(int(tnums[k]))
            
    # Get immidiate smaller element on right otherwise store n at the position
    smallOnRight = [(n,0)]*n
    stack = []
    s = 0
    while s < n:
        if len(stack) == 0:
            stack.insert(0, (s, nums[s]))
        topEle = stack[0][1]
        if nums[s] >= topEle:
            stack.insert(0, (s, nums[s]))
            s += 1
        else:
            (i, v) = stack.pop(0)
            smallOnRight[i] = (s, nums[s])
    #print(smallOnRight)
    
    # Get immidiate smaller elemnt on left otherwise store -1 at the position
    smallOnLeft = [(-1, 0)]*n
    stack = []
    s = n - 1
    while s >= 0:
        if len(stack) == 0:
            stack.insert(0, (s, nums[s]))
        topEle = stack[0][1]
        if nums[s] >= topEle:
            stack.insert(0, (s, nums[s]))
            s -= 1
        else:
            (i, v) = stack.pop(0)
            smallOnLeft[i] = (s, nums[s])
    #print(smallOnLeft)
    
    # the difference of indexes the range in which given is guranteed to be smallest
    fArr = [0]*(n+1)
    for k in range(0, n):
        rlen = smallOnRight[k][0] - smallOnLeft[k][0] - 1 
        fArr[rlen] = max(fArr[rlen], nums[k])
        
    for k in range(n-1,-1,-1):
        fArr[k] = max(fArr[k], fArr[k+1])
    
    res.append(' '.join( str(x) for x in fArr[1:]))
    
for xx in res:
    print(xx)
