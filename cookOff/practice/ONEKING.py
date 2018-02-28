'''
Created on 10-Aug-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    heap = []
    n = int(input())
    for j in range(0, n):
        (m,n1) = input().split(" ")
        heap.append((int(m), int(n1)))
        
    heap.sort(key=lambda x:x[1])
    bomb = 0
    fi = -1
    for (m, n) in heap:
        if m > fi:
            fi = n
            bomb += 1
    results.append(bomb)
    
    
for xx in results:
    print(xx)