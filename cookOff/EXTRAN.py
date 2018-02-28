'''
Created on 04-Mar-2017

@author: rjoshi
'''
tests = int(input())
results = []
def nsum(n):
    if n % 2 == 0:
        return int((n/2)*(n+1))
    else:
        return int(((n+1)/2)*n)
    
for t in range(0, tests):
    n = int(input())
    nums = input().split(" ")
    l1 = l2 = 0
    totalSum = 0
    for k in range(0, n):
        c = int(nums[k])
        totalSum = totalSum + c
        if k == 0:
            l1 = l2 = c
        elif l1 == l2 and l1 != 0 and c > l1:
            l2 = c
        elif c < l1:
            l2 = l1
            l1 = c
        elif c < l2 and c > l1:
            l2 = c
    
    expectedSum = 0
    if l2 - l1 != 1:
        results.append(l1)
    else:
        expectedSum = l1*(n-1) + nsum(n-2)
        for k in range(0, n):
            c = int(nums[k])
            if totalSum - c == expectedSum:
                results.append(c)
                break      
for xx in results:
    print(xx) 
            