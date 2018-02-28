'''
Created on 21-Dec-2017

@author: rjoshi
'''

def getSmallestWindow(mainStr, subStr):
    if len(subStr) > len(mainStr):
        return -1
    
    subStrCountDict = [0]*200
    for i in range(0, len(subStr)):
        iStr = ord(subStr[i])
        subStrCountDict[iStr] += 1
        
    matchedStrCountDict = [0]*200
    start = 0
    maxLenWindow = 10000
    starti = 0
    count = 0
    
    for i in range(0, len(mainStr)):
        iStr = ord(mainStr[i])
        matchedStrCountDict[iStr] += 1
        
        if subStrCountDict[iStr] >= matchedStrCountDict[iStr]:
            count += 1
            
        if count == len(subStr):
            
            iStr = ord(mainStr[start])
            while (matchedStrCountDict[iStr] > subStrCountDict[iStr]
                   or subStrCountDict[iStr] == 0):
                if matchedStrCountDict[iStr] > subStrCountDict[iStr]:
                    matchedStrCountDict[iStr] -= 1
                start += 1
                iStr = ord(mainStr[start])
            
            windowLen = i - start + 1
            if windowLen < maxLenWindow:
                maxLenWindow = windowLen
                starti = start
                    
    return mainStr[starti: starti + maxLenWindow]

mainStr = "this is a test string"
subStr = "test"
print(getSmallestWindow(mainStr, subStr))

                
                