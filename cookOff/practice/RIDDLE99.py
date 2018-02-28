'''
Created on 02-Jul-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    nums = input().split(" ")
    s = int(nums[0])
    e = int(nums[1])
    d = int(nums[2])
    
    if e < d:
        results.append(0)
    elif s == e and e == d:
        results.append(1)
    else:
        q = s % d
        if q == 0:
            diff = e - s
        else:
            diff = e - (s+ (d-q))
        results.append(1 + int(diff/d))
                       
for xx in results:
    print(xx)