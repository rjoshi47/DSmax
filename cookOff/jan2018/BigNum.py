'''
Created on 05-Jan-2018

@author: rjoshi
'''
def bSearch(arr, num, l, r):
    if l > r:
        return -1
    else:
        m = int((l+r)/2)
        if m == l:
            if l+1 <= r and int(arr[m]) < num and int(arr[l+1]) >= num:
                return m
            elif m+1 == r and int(arr[r]) < num:
                return m+1
            else:
                return -1
        elif m == r:
            if int(arr[m]) < num:
                return m
            else:
                return -1
        elif int(arr[m]) < num:
            if m == r:
                return m
            elif m+1 <= r and int(arr[m+1]) >= num:
                return m
            else:
                return bSearch(arr, num, m, r)
        else:
            return bSearch(arr, num, l, m)

tests = int(input())
res = []
for x in range(0, tests):
    n = int(input())
    arrDict = {}
    stack = []
    for j in range(0, n):
        nums = input().split(" ")
        nums.sort(key=int)
        arrDict[j] = nums
    
    larr = arrDict[n-1]
    stack.append(larr[n-1])
    for k in range(n-2,-1,-1):
        num = int(stack[len(stack)-1])
        nArr = arrDict[k]
        ret = bSearch(nArr, num, 0, n-1)
        if ret == -1:
            break
        else:
            stack.append(nArr[ret])
    
    if len(stack) != n:
        res.append(-1)
    else:
        msum = 0
        for m in range(0, len(stack)):
            msum += int(stack[m])
        res.append(msum)
        
for xx in res:
    print(xx)