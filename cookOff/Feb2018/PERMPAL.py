'''
Created on 04-Feb-2018

@author: rjoshi
'''
res = []
def getChrDict():
    cDict = {}
    for i in range(97, 123):
        cDict[chr(i)] = (0, 0)
    return cDict

def checkPalindromIdx(rstr, idxList):
    l = 0
    r = len(rstr) - 1
    while l < r:
        if idxList[l] == '' or idxList[r] == '':
            return False
        if rstr[idxList[l]] != rstr[idxList[r]]:
            return False
        l += 1
        r -= 1
    return True

def getResult(idxList):
    result = ''
    for i in range(0, len(idxList)):
        val = idxList[i] + 1
        if i != len(idxList) - 1:
            result += str(val) + ' '
        else:
            result += str(val)
    return result

def checkPalindrom(rstr):
    l = 0
    r = len(rstr) - 1
    while l < r:
        if rstr[l] != rstr[r]:
            return False
        l += 1
        r -= 1
    return True

for oo in range(0, int(input())):
    iStr = input()
    palStr = ['']*len(iStr)
    palIdx = ['']*len(iStr)
    charCountDict = getChrDict()
    
    pi = 0
    for k in range(0, len(iStr)):
        if charCountDict[iStr[k]][0] == 0:
            charCountDict[iStr[k]] = (1, k)
        else:
            rpi = len(iStr) - 1 - pi
            
            idx = charCountDict[iStr[k]][1]
            palIdx[rpi] = idx
            palIdx[pi] = k
            
            charCountDict[iStr[k]] = (0, 0)
            
            palStr[rpi] = iStr[k]
            palStr[pi] = iStr[k]
            pi += 1
    
    oddChr = ''
    oddIdx = -1
    for k in range(0, len(iStr)):
        if charCountDict[iStr[k]][0] != 0:
            if oddChr == '':
                oddChr = iStr[k]
                oddIdx = charCountDict[iStr[k]][1]
            else:
                break
    
    if oddChr != '' and len(iStr) % 2 != 0:
        palStr[int(len(iStr)/2)] = oddChr
        palIdx[int(len(iStr)/2)] = oddIdx
    
    if checkPalindrom(palStr) and checkPalindromIdx(iStr, palIdx):
        #res.append(palStr)
        #res.append(palIdx)
        #res.append(" ")
        res.append(getResult(palIdx))
    else:
        res.append(-1)
    
for xx in res:
    print(xx)
        
        
    