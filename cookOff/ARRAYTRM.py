'''
Created on 18-Mar-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    (n, k) = input().split(" ")
    n = int(n)
    k = int(k)+1
    nums = input().split(" ")
    count1 = 0
    count2 = 0
    c1 = int(nums[0]) % k
    c2 = -1
    for j in range(0, int(n)):
        numi = int(nums[j])
        if numi % k == c1:
            count1 = count1 + 1
        elif numi % k == c2:
            count2 = count2 + 1
        elif c2 == -1:
            count2 = count2 + 1
            c2 = numi%k
        else:
            break
    if j < int(n) - 1:
        results.append("NO")
    elif count1 == n or count1 == n-1 or count2 == n-1:
        results.append("YES")
    else:
        results.append("NO")
        
for xx in results:
    print(xx)