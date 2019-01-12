'''
Created on May 10, 2018
https://practice.geeksforgeeks.org/problems/special-keyboard/0
@author: devuser
'''

def getMaxAs(n, cv, clipBoard):
    print((n, cv, clipBoard))
    if n == 0:
        return cv
    if vPress != 0: # 
        return getMaxAs(n-1, cv+1, clipBoard)
    elif vPress == 0:
        if n >= 3:
            return max(getMaxAs(n-1, cv+1, clipBoard), getMaxAs(n-3, 2*cv, cv))
        else:
            return n+cv
    

res = []
for _ in range(int(input())):
    n = int(input())
    res.append(getMaxAs(n, 0, 0))
    
for xx in res:
    print(xx)
