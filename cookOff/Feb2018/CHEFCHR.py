'''
Created on 03-Feb-2018

@author: rjoshi
'''

def checkStr(tStr):
    cDict = {}
    cDict['c'] = 0
    cDict['h'] = 0
    cDict['e'] = 0
    cDict['f'] = 0
    
    for i in range(0, len(tStr)):
        if tStr[i] not in cDict:
            break
        else:
            cDict[tStr[i]] = 1
    
    count = cDict['c'] + cDict['h'] + cDict['e'] + cDict['f']
    if count == 4:
        return True
    else:
        return False
    
    
tHash = ord('c') + ord('h') + ord('e') + ord('f')  
res = []
for i in range(0, int(input())):
    istr = input()
    count = 0
    
    if len(istr) > 3:
        tsum = 0
        for j in range(0, 4):
            tsum += ord(istr[j])
        
        if tsum == tHash and checkStr(istr[0:4]):
            count += 1
        
        tail = 0
        
        for j in range(4, len(istr)):
            if j - tail == 4:
                tsum += ord(istr[j]) - ord(istr[tail])
                if tsum == tHash and checkStr(istr[tail+1:j+1]):
                    count += 1
                tail += 1
                
    if count > 0:
        res.append("lovely "+str(count))
    else:
        res.append("normal")
        
for xx in res:
    print(xx)