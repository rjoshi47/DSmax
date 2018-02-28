'''
Created on 07-May-2017

@author: rjoshi
'''

def getLongestPalinLength(arrStr):
    myGraph = {}
    temp = []
    temp.append('$')
    for i in range(0, len(arrStr)):
        temp.append('#')
        temp.append(arrStr[i])
    temp.append('#')
    temp.append('@')
    
    p = [0]*len(temp)
    
    c = 0
    r = 0
    print(temp)
    for i in range(1, len(temp)-1):
        mirror = 2*c - i
        
        if mirror < c:
            p[i] = min(r-i, p[mirror])
            
        while temp[i + p[i] + 1] == temp[i - (p[i] + 1)]:
            p[i] = p[i] + 1
        if i + p[i] > r:
            c = i 
            r = i + p[i]
    print(p[c])
#         if p[i] > 0:    
#             print(i,end=" ")
#             print((r, (i-p[i], i+p[i])))
#             if i-p[i] not in myGraph:
#                 l = []
#                 l.append(i+p[i])
#                 myGraph[i-p[i]] = l
#             else:
#                 l = myGraph[i-p[i]]
#                 l.append(i+p[i])
#                 myGraph[i-p[i]] = l
        
    
    #print(arrStr)
    print(p)
    print(myGraph)
    return p[c]
    
            
getLongestPalinLength('EABAEABAB')
getLongestPalinLength('AAAAAAA')