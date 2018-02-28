'''
Created on 06-Nov-2017

@author: rjoshi
'''
tests = int(input())
results = []
def isPalin(sss):
    l = 0
    r = len(sss) - 1
    while l <= r:
        if sss[l] != sss[r]:
            return False
        l += 1
        r -= 1 
    return True

for i in range(0, tests):
    (N, P) = input().split(" ")
    n = int(N)
    p = int(P)
    
    if p == 1 or p == 2 or n == 1:
        results.append("impossible")
    elif n == p:
        pal = ""
        c = n - 2
        pal = 'a'
        while c > 0:
            pal += 'b'
            c -= 1
        pal += 'a'
        results.append(pal)
    else:
        m = int(n/p) - 1
            
        pal = ""
        c = p - 2
        pal = 'a'
        while c > 0:
            pal += 'b'
            c -= 1
        pal += 'a'
        
        palf = pal
        while m > 0:
            palf += pal
            m -= 1
        if len(palf) == n and isPalin(palf):
            results.append(palf)
        else:
            results.append("impossible")
            
for xx in results:
    print(xx)