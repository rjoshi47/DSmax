'''
Created on 06-Dec-2017
 
@author: rjoshi
'''
tests = int(input())
results = []
for i in range(0, tests):
    n = int(input())
    numso = input().split(" ")
    nums = list(numso)
    n = len(nums)
    l = 0
    r = n - 1
    
    while l < r:
        if nums[l] != nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        else:
            if l+1 < r-1:
                nums[l], nums[l+1] = nums[l+1], nums[l]
                nums[r], nums[r-1] = nums[r-1], nums[r]
                l += 2
                r -= 2
            elif l-1 >= 0 and r + 1 <= n - 1:
                nums[l], nums[l-1] = nums[l-1], nums[l]
                nums[r], nums[r+1] = nums[r+1], nums[r]
                l += 2
                r -= 2
            else:
                break
            
    if n % 2 == 1 and n >= 3:
        m = int(n/2)
        mv = nums[m]
        
        for p in range(0, n):
            if mv != nums[p] and mv != numso[p]:
                nums[m], nums[p] = nums[p], nums[m]
                break
            
    
    dist = 0
    for p in range(0, n):
        if nums[p] != numso[p]:
            dist += 1
            
    results.append(dist)
    results.append(' '.join(nums))
 
for i in range(0, len(results)):
    if i % 2 == 1:
        print(results[i])
    else:
        ll = results[i]
        print(ll) 