'''
Created on 07-Jul-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    signs = input()
    counter = 0
    smallest = 0
    largest = 0
    start = 0
    pSmall = 0
    pLarge = 0
    psymb = ''
    for j in range(0, len(signs)):
        symb = signs[j].strip()
        if symb == '=':
            continue
        
        tcount = 0
        if psymb != '' and psymb != symb:
            if smallest == 0:
                tcount = largest + 1
            elif smallest < 0:
                tcount = 1 + abs(smallest)+largest
            start = 0
            smallest = 0
            largest = 0
            if tcount > counter:
                counter = tcount
        psymb = symb
        if symb == '>':
            start = start - 1
            if start < smallest:
                smallest = start;
        elif symb == '<':
            start = start + 1
            if start > largest:
                largest = start;
    
    if counter > 0:
        if counter > 1 + abs(smallest)+largest:
            results.append(counter)
        else:
            results.append(1 + abs(smallest)+largest)
    elif smallest == 0:
        results.append(largest + 1)
    elif smallest < 0:
        results.append(1 + abs(smallest)+largest)

for xx in results:
    print(xx)