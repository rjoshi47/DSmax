'''
Created on 08-Nov-2017

@author: rjoshi
'''
tests = int(input())
res = []
for i in range(0, tests):
    (n, m) = input().split(" ")
    n = int(n)
    m = int(m)
    
    plen = 0
    pal = ''
    
    if m == 1:
        plen = n
        for k in range(0, n):
            pal += 'a'
    elif m == 2:
        if n == 1:
            plen = 1
            pal = "a"
        elif n == 2:
            plen = 1
            pal = "ab"
        elif n == 3:
            plen = 2
            pal = "abb"
        elif n == 4:
            plen = 2
            pal = 'aabb'
        elif n == 5:
            plen = 3
            pal = 'aabbb'
        elif n == 6:
            plen = 3
            pal = 'aaabbb'
        elif n == 7:
            plen = 3
            pal = 'aababbb'
        elif n == 8:
            plen = 3
            pal = 'aaababbb'
        else:
            plen = 4
            arr = ['a', 'b','b','a','a', 'b']
            for k in range(0, n):
                pal += arr[k%6]
    elif m > 2:
        plen = 1
        k = 1
        for k in range(0, n):
            if k % 3 == 0:
                pal += 'a'
            elif k % 3 == 1:
                pal += 'b'
            elif k % 3 == 2:
                pal += 'c'
    res.append((plen, pal))

for (x, y) in res:
    print(x, end=" ")
    print(y)        
            
        
                    