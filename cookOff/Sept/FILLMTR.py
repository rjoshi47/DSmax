'''
Created on 02-Sep-2017

@author: rjoshi
'''
tests = int(input())
res = []
for p in range(0, tests):
    (n, q) = input().split(" ")
    mDict = {}
    found = 1
    lst = []
    for k in range(0, int(q)):
        (i, j, v) = input().split(" ")
        i = int(i)
        j = int(j)
        v = int(v)
        if i == j and v != 0:
            found = 0
        if (j,i) in mDict and mDict[(j,i)] != v:
            found = 0
        lst.append((i,j))
        mDict[(i,j)] = int(v)
    
    for (i,j) in lst:
        mDict[(j,i)] = mDict[(i,j)]
    
    if found == 1:
        for m in range(2, int(n)):
            for n1 in range(m+1, int(n)+1):
                if (m,n1) in mDict:
                    a = mDict[(m,n1)]
                    if (m-1, m) in mDict and (m-1, n1) in mDict:
                        if abs(a) != abs(mDict[(m-1, m)] - mDict[(m-1, n1)]):
                            found = 0
                            break
                elif (m-1, m) in mDict and (m-1, n1) in mDict:
                    mDict[(m,n1)] = (mDict[(m-1, m)] - mDict[(m-1, n1)])
                    mDict[(n1,m)] = mDict[(m,n1)]
            if found == 0:
                break
#         for m in range(2, int(n)):
#             for n1 in range(m+1, int(n)+1):
#                 print(mDict[(m,n1)], end=' ')
#             print()
                    
    if found == 1:
        res.append("yes")
    else:
        res.append("no")            
    
        
for xx in res:
    print(xx)