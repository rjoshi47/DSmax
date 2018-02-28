'''
Created on 28-May-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    n = int(input())
    r1 = input()
    r2 = input()
    d1 = {}
    d2 = {}
    len = 0
    s1 = -1
    e1 = -1
    i = 0
    while i < n:
        if r1[i] == '#':
            f1 = i
            while i < n and r1[i] == '#':
                i = i + 1
            if f1 != i:
                if s1 == -1:
                    s1 = f1
                len = len + abs(f1 - i)
            if i >= n-1:
                break
        else:
            i = i + 1
    s2 = -1
    e2 = -1
    i = 0
    while i < n:
        if r2[i] == '#':
            f1 = i
            while i < n and r2[i] == '#':
                i = i + 1
            if f1 != i:
                if s2 == -1:
                    s2 = f1
                len = len + abs(f1 - i)
            if i >= n-1:
                break
        else:
            i = i + 1
    mlen = 0
    if s2 == -1 and s1 != -1:
        while s1 < n and r1[s1] == '#':
            mlen = mlen + 1
            s1 = s1 + 1
        if mlen == len:
            results.append("yes")
        else:
            results.append("no")
    elif s1 == -1 and s2 != -1:
        while s2<n and r2[s2] == '#':
            mlen = mlen + 1
            s2 = s2 + 1
        if mlen == len:
            results.append("yes")
        else:
            results.append("no")
    else:
        mlen = 1
        if s1 < s2:
            flag = True
            cp = r1
            c = s1
        else:
            flag = True
            cp = r2
            c = s2
        while True and c < n and (r1[c] == '#' or r2[c] == '#'):
            if cp == r1:
                #print(c)
                if flag == True and r2[c] == '#':
                    cp = r2
                    flag = False
                    mlen = mlen + 1
                elif c+1 < n and r1[c+1] == '#':
                    c = c + 1
                    mlen = mlen + 1
                    flag = True
                else:
                    break
            else:
                #print(c)
                if flag == True and r1[c] == '#':
                    cp = r1
                    flag = False
                    mlen = mlen + 1
                elif c+1 < n and r2[c+1] == '#':
                    c = c + 1
                    mlen = mlen + 1
                    flag = True
                else:
                    break
        if s1 == s2 and len != mlen:
            mlen = 1
            flag = True
            cp = r1
            c = s1
            while True and c < n and (r1[c] == '#' or r2[c] == '#'):
                if cp == r1:
                    #print(c)
                    if flag == True and r2[c] == '#':
                        cp = r2
                        flag = False
                        mlen = mlen + 1
                    elif c+1 < n and r1[c+1] == '#':
                        c = c + 1
                        mlen = mlen + 1
                        flag = True
                    else:
                        break
                else:
                    #print(c)
                    if flag == True and r1[c] == '#':
                        cp = r1
                        flag = False
                        mlen = mlen + 1
                    elif c+1 < n and r2[c+1] == '#':
                        c = c + 1
                        mlen = mlen + 1
                        flag = True
                    else:
                        break
                
        if len == mlen:
            results.append("yes")               
        else:
            results.append("no")
                
                
                
                
for xx in results:
    print(xx)