'''
Created on 21-Jan-2018

@author: rjoshi
'''
res = []
tests = int(input())
for i in range(0, tests):
    n = int(input())
    nums = input().split(" ")
    
    if n == 1:
        res.append(0)
    elif n == 2:
        if n[0] != n[1]:
            res.append(0)
        else:
            res.append(-1)
    elif n % 2 == 0:
        l = 0
        r = n - 1
        while l < r:
            if 