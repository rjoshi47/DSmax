'''
Created on 20-May-2018

@author: rjoshi
'''

def getPrimesTillN(n):
    nsq = int(pow(n, 0.5))
    primes = [True]*(n+1)
    
    for p in range(2, nsq+1):
        if primes[p] == True:
            for i in range(2*p, n+1, p):
                primes[i] = False
    
    return primes

primes = getPrimesTillN(400)

def getPrimes(n):
    nums = []
    for k in range(2, len(primes)):
        if k > n:
            break
        if primes[k]:
            nums.append(k)
    return nums

res = []
for _ in range(0, int(input())):
    n = int(input())
    f = ''
    nums = getPrimes(n)
    for k in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[k]*nums[j] <= n:
                f += ' ' + str(nums[k]) + ' '+str(nums[j])
    res.append(f.strip())
    
for xx in res:
    print(xx)
