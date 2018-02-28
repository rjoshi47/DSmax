'''
Created on 02-Mar-2017

@author: rjoshi
'''
def getHash(num,size):
    numStr = str(num)
    hashVal = 0
    for i in range(0, len(numStr)-1):
        hashVal = hashVal + ord(numStr[i])
    return hashVal 

def getNextSeq(srch, num, interval, size):
    numStr = str(num)
    if interval+size-1 >= len(numStr):
        return -1
    firstDigitRemoved0 = int(numStr[interval:interval+size-1])*10
    firstDigitRemoved0 = firstDigitRemoved0 + int(numStr[interval+size-1])
    return getHash(firstDigitRemoved0, size)
    
mainStr = 12345678934567221134
srchStr = 5672
size = len(str(srchStr))
srchStrhash = getHash(srchStr, size)
for i in range(0, len(str(mainStr))):
    seqHash = getNextSeq(srchStr,mainStr, i, size)
    if seqHash == -1:
        print("no match")
        break
    elif seqHash == srchStrhash and str(mainStr)[i:i+size] == str(srchStr):
        print(str(mainStr)[i:i+size]+" match "+str(i))
        break
        