'''
Created on 01-Sep-2017

@author: rjoshi
'''

tests = int(input())
res = []
for i in range(0, tests):
    n = int(input())
    nums = input().split(" ")
    min1 = 10000000
    idx = 0
    for k in range(0, n):
        val = int(nums[k])
        if val < min1:
            min1 = val
            idx = k
    res.append(idx+1)

for xx in res:
    print(xx)