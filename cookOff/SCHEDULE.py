'''
Created on 11-Mar-2017

@author: rjoshi
'''
numPos = {}
boundary = []
def getGroups(n, l):
    n2 = int(n/2)
    return (n2 - (n2 - l), (n2 -l))
def newNextFlip(n, k, nk):
    global numPos
    global boundary
    if n%2 == 0 and n in boundary:
        for m in range(0, k):
            (p, q) = getGroups(n+1, m)
            if nk > 0 and q <= nk:
                break
        if p > 0 and 1 not in numPos:
            numPos[1] = 1
        elif p > 0:
            count = numPos[1] + p*1
            numPos[1] = count
        
        if q > 0 and q not in numPos:
            numPos[q] = 2
        elif q > 0:
            count = numPos[q] + 2
            numPos[q] = count
        if n in boundary:
            boundary.remove(n)
            boundary.append(q)
        return (p, q, m+1)
    elif n%2 == 0:
        m = int(n/2)
        if m not in numPos:
            numPos[m] = 1
        else:
            count = numPos[m]
            numPos[m] = count + 1
        
        if m-1 not in numPos:
            numPos[m-1] = 1
        else:
            count = numPos[m-1]
            numPos[m-1] = count + 1
        if n in boundary:
            if len(boundary) == 1:
                boundary.append(m)
            boundary.remove(n)
            boundary.append(m-1)
        return (m, m-1,1)
        
    if n > 2:
        if n % 2 != 0:
            for m in range(0, k):
                (p, q) = getGroups(n, m)
                if nk > 0 and q <= nk:
                    break
            if p > 0 and 1 not in numPos:
                numPos[1] = 1
            elif p > 0:
                count = numPos[1] + p*1
                numPos[1] = count
            
            if q > 0 and q not in numPos:
                numPos[q] = 2
            elif q > 0:
                count = numPos[q] + 2
                numPos[q] = count
            if n in boundary:
                boundary.remove(n)
                boundary.append(q)
            return (p, q, m+1)
        
def nextFlip(n):
    if n > 2:
        m = int(n/2)
        if n % 2 == 0:
            return (m, m-1)
        else:
            return (n-2, 1)

def getNums(numStr):
    l = len(numStr)
    nums = []
    i = 0
    while i < l:
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
            numPos[c] = 1
        else:
            count = numPos[c]
            numPos[c] = count + 1
        nums.append(c)
    return nums

def flipOp(numStr, k):
    global numPos;
    global boundary;
    boundary = []
    numPos = {}
    nums = getNums(numStr)
    if len(nums) > 1:
        boundary.append(nums[0])
        boundary.append(nums[len(nums)-1])
    else:
        boundary.append(nums[0])
    keys = list(reversed(sorted(numPos.keys())))
    
#     print(nums)
#     print(numPos)
#     print(keys)
#     print(boundary)
    
    i = 0
    while k > 0 and keys[i] != None:
        key = keys[i]
        nk = 0
        if len(keys) > 1:
            nk = keys[i+1]
        if key == 1:
            return 1
        flips = numPos.pop(key)
        keys.remove(key)
        if flips > k:
            return key
        else:
            #k = k - flips
            for j in range(0, flips):
                if key == 2:
                    if 2 in boundary:
                        boundary.remove(2)
                        boundary.append(1)
                        if j == flips - 1:
                            return '1'
                    else:
                        return '2'
                    k = k -1
                else:
                    (m, n, v) = newNextFlip(key, k, nk)
                    k = k - v
        if numPos == {} or k < 0:
            return 1
        keys = list(reversed(sorted(numPos.keys())))
    return keys[0]

#print(flipOp("100101100000001", 3))
         
results = []
tests = int(input())
for i in range(0, tests):
    ab = input().split(" ")
    nums = input()
    results.append(flipOp(nums, int(ab[1])))
            
for xx in results:
    print(xx)
