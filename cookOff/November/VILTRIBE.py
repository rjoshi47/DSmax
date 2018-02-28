'''
Created on 05-Nov-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    vills = input()
    
    villMap = {}
    villMap['A'] = 0
    villMap['B'] = 0
    
    i = 0
    count = 0
    preV = 'NA'
    for k in range(0, len(vills)):
        if vills[k] == '.' and preV == 'NA':
            continue
        
        if vills[k] == '.':
            count += 1
        elif vills[k] == 'A':
            if preV == 'NA':
                villMap['A'] = villMap['A'] + 1
                preV = 'A'
            elif preV == 'A':
                if count > 0:
                    villMap['A'] = villMap['A'] + count + 1
                    count = 0
                else:
                    villMap['A'] = villMap['A'] + 1
            elif preV == 'B':
                preV = 'A'
                count = 0
                villMap['A'] = villMap['A'] + 1
        else:
            if preV == 'NA':
                villMap['B'] = villMap['B'] + 1
                preV = 'B'
            elif preV == 'B':
                if count > 0:
                    villMap['B'] = villMap['B'] + count + 1
                    count = 0
                else:
                    villMap['B'] = villMap['B'] + 1
            elif preV == 'A':
                preV = 'B'
                count = 0
                villMap['B'] = villMap['B'] + 1
                
    results.append((villMap['A'], villMap['B']))
    
for (x, y ) in results:
    print(x, end=" ")
    print(y)