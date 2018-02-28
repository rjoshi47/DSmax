'''
def getNums(numStr):
    l = len(numStr)
    nums = []
    i = 0
    while i < l:
        print(i)
        if numStr[i] == '0':
            c = 0
            while i < l and numStr[i] == '0':
                c = c + 1
                i = i + 1
        elif numStr[i] == '1':
            c = 0
            while i < l and numStr[i] == '1':
                c = c + 1
                i = i +1
        if c not in numPos:
            pos = [len(nums)]
            numPos[c] = pos
        else:
            pos = numPos[c]
            pos.append(len(nums))
            numPos[c] = pos
        nums.append(c)
    return nums
Created on 05-Mar-2017

@author: rjoshi
'''
def getBand(n, ones):
    for i in range(1,n):
        if ones - (2*(n-i)) <= 0:
            return i
        else:
            ones = ones - (2*(n-i))
        
tests = int(input())
results = []
for k in range(0, tests):
    n = int(input())
    do = 0
    ndo = 0
    for i in range(0,n):
        nums = input().split(" ")
        for j in range(0,n):
            if i == j and nums[j] == '1':
                do = do + 1
            elif nums[j] == '1':
                ndo = ndo + 1
    ones = ndo - (n-do)
    if ndo + do <= n:
        results.append(0)
    else:
        results.append(getBand(n, ones))
    
for xx in results:
    print(xx)
    