'''
Created on 11-Jun-2017

@author: rjoshi
'''   
res = []  
tests = int(input())
for i in range(0,tests):
    (n,k) = input().split(" ")
    sum1 = 0
    n = int(n)
    k1 = int(k)
    arrD = {}
    for k in range(0, n):
        arrD[k] = input().split(" ")
    removed = []
    for k in range(0, n):
        if k not in removed:
            a1 = arrD[k]
            fnum = []
            for i in range(0, len(a1)):
                if int(a1[i]) not in fnum and int(a1[i]) <= k1:
                    fnum.append(int(a1[i]))
                if len(fnum) >= k1:
                    break
                
            if len(fnum) >= k1:
                sum1 = sum1 + (n-k-1)
                removed.append(k)
            elif k+1 < n:
                for p in range(k+1,n):
                    if p not in removed:
                        fnumCopy = []
                        fnumCopy = fnum.copy()
                        a2 = arrD[p]
                        for i in range(0, len(a2)):
                            if int(a2[i]) not in fnumCopy and int(a2[i]) <= k1:
                                fnumCopy.append(int(a2[i]))
                            if len(fnumCopy) >= k1:
                                break
                        if len(fnumCopy) >= k1:
                            sum1 = sum1 + 1
        if k not in removed:
            removed.append(k)
    res.append(sum1)

for xx in res:
    print(xx)                        
    
                        
                        
                        
                        
            