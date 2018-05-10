'''
Created on May 10, 2018

@author: devuser
'''

def getMaxAs(n, cv, vPress):
    print((n, cv, vPress))
    if n == 0:
        return cv
    if vPress != 0:
        return getMaxAs(n-1, cv+1, vPress)
    elif vPress == 0:
        if n >= 3:
            return max(getMaxAs(n-1, cv+1, vPress), getMaxAs(n-3, 2*cv, cv))
        else:
            return n+cv
    
    '''
    if n == 0:
        return cv
    if n > 3:
        if vPress == 0:
            return max(getMaxAs(n-1, cv+1, vPress), getMaxAs(n-3, 2*cv, cv))
        else:
            return getMaxAs(n-1, cv + vPress, vPress)
            #return max(getMaxAs(n-1, cv+1, vPress), getMaxAs(n-1, cv + 2*vPress, vPress))
    else:
        if vPress != 0:
            return getMaxAs(n-1, cv + vPress, vPress)
        else:
            return (n + cv)
    '''
res = []
for _ in range(int(input())):
    n = int(input())
    res.append(getMaxAs(n, 0, 0))
    
for xx in res:
    print(xx)
