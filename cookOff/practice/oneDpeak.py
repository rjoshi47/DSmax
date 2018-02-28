'''
Created on 14-Jun-2017

@author: rjoshi
'''

def findPeak(n, s, e):
    if e - s == 1:
        if n[e] > n[s]:
            return n[e]
        else:
            return n[s]
    m = int((e+s)/2)
    if m == s and len(n) > 1:
        if n[s] >= n[s+1]:
            return n[0]
    if m == e and len(n) > 1:
        if n[e] >= n[e-1]:
            return n[e]
    if n[m] < n[m+1]:
        return findPeak(n, m, e)
    if n[m-1] > n[m]:
        return findPeak(n, s, m-1)
    else:
        return n[m]
    
n = [10,19,8,7,6,14,23,32,111]
print(findPeak(n, 0, len(n)-1)) 