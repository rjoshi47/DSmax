'''
Created on 03-Dec-2017

@author: rjoshi
'''

tests = int(input())
results = []
for i in range(0, tests):
    (n, m) = input().split(" ")
    n = int(n)
    m = int(m)
    cr = 0
    cg = 0
    
    for r in range(0, n):
        row = input()
        for c in range(0, m):
            cval = row[c]
            if r % 2 == 0:
                if c%2 == 0:
                    if cval == 'R':
                        cg += 5
                    else:
                        cr += 3
                else:
                    if cval == 'R':
                        cr += 5
                    else:
                        cg += 3
            else:
                if c%2 == 0:
                    if cval == 'R':
                        cr += 5
                    else:
                        cg += 3
                else:
                    if cval == 'R':
                        cg += 5
                    else:
                        cr += 3
    results.append(min(cg, cr))
    
for xx in results:
    print(xx)
                    