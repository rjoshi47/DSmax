'''
Created on 08-Jul-2017

@author: rjoshi
'''
res = []
tests = int(input())
for i in range(0, tests):
    (s, d) = input().split(" ")
    s = int(s)
    d = int(d)
    
    res2 = res3 = res1 = 0
    
    fm2 = int(s/2)
    res2 = fm2*(int((s - fm2)/d))
    
    vm2 = s - fm2
    div = int(vm2/d)    
    fm1 = s - d*(div+1)
    if fm1 > 0:
        res1 = fm1*(int((s - fm1)/d))
    
    if vm2/d > 1:
        if div == vm2/d:
            fm3 = s - d*(div-1)
        else:
            fm3 = s - d*(div)
        res3 = fm3*(int((s - fm3)/d))
   
    if res1 > res2:
        if res1 > res3:
            res.append(res1)
        else:
            res.append(res3)
    else:
        if res2 > res3:
            res.append(res2)
        else:
            res.append(res3)
    
for ss in res:
    print(ss)