'''
Created on Apr 30, 2018

@author: rjoshi

for nchars: abcabceabcabce
rep = [0, 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7]
patLen = 7

For string to be valid the last value of rep array must be a multiple of pattern length.
E.g.
nchars: abcabceabcabceabcabce
rep = [0, 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
patLen = 7
'''
def isRepeated(nchars):
    rep = [0]*len(nchars)
    
    k = 1 
    s = 0
    mcount = 1
    patLen = 0
    while k < len(nchars):
        if nchars[k] == nchars[s]:
            rep[k] = mcount
            s += 1
            mcount += 1
        else:
            patLen = k + 1
            mcount = 1
            s = 0
        k += 1
        
    return rep[len(nchars)-1] != 0 and ((rep[len(nchars)-1] == len(nchars)-1)
            or rep[len(nchars)-1] % patLen == 0)
    

res = [] 
for _ in range(0, int(input())):
    res.append(isRepeated(input().strip()))
    
for xx in res:
    print(xx)
