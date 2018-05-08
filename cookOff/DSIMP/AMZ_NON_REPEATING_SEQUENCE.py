'''
Created on 08-May-2018
https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring/0
@author: rjoshi
'''
res = []
for _ in range(0, int(input())):
    mstr = input().strip()
    lastCharIndex = {}
    lastCharIndex[mstr[0]] = 0
    
    count = 0
    s = 0
    e = 0
    
    for e in range(1, len(mstr)):
        if mstr[e] in lastCharIndex and lastCharIndex[mstr[e]] >= s:
            s = lastCharIndex[mstr[e]] + 1    
        tCount = e - s + 1
        count = max(count, tCount) 
        lastCharIndex[mstr[e]] = e
        
    res.append(count)
    
for xx in res:
    print(xx)
