'''
Created on 06-Nov-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    (n, val) = input().split(" ")
    nums = input().split(" ")
    
    val = int(val)
    n = len(nums)
    
    h = -1
    l = -1
    
    f = 1
    for k in range(0, n):
        cval = int(nums[k])
        if cval == val:
            f = 1
            break
        
        if cval > val:
            if h == -1:
                h = cval
            elif cval > h:
                f = 0
                break
            else:
                h = cval
        else:
            if l == -1:
                l = cval
            elif cval < l:
                f = 0
                break
            else:
                l = cval
    if f == 1:
        results.append("YES")
    else:
        results.append("NO")
        
for xx in results:
    print(xx)