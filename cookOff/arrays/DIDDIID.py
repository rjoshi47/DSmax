'''
Created on 14-Oct-2017

@author: rjoshi
'''

def processDI(arr):
    tempArr = [0]
    finalArr = []
    maxTillNow = 0
    prevSymb = arr[0]
    for i in range(0, len(arr)):
        if prevSymb == 'D':
            if arr[i] == 'D':
                tempArr.append(tempArr[len(tempArr)-1] -1)
            else:
                minELe = tempArr[0]
                for i in range(0, len(tempArr)):
                    if tempArr[i] < minELe:
                        minELe = tempArr[i]
                        
                maxEle = 0
                for i in range(0, len(tempArr)):
                    ele = maxTillNow + (-minELe) + 1 + tempArr[i]
                    if ele > maxEle:
                        maxEle = ele
                    finalArr.append(ele)
                if maxEle > maxTillNow:
                    maxTillNow = maxEle
                tempArr = [0]
                prevSymb = 'I'
                
        elif prevSymb == 'I':
            if arr[i] == 'D':
                tempArr.append(tempArr[len(tempArr)-1] - 1)
            else:
                if i+1 < len(arr) and arr[i+1] != 'D':
                    tempArr.append(tempArr[len(tempArr)-1] + 1)
                    
    print(finalArr)        
    
arr = list("DDI")
processDI(arr)
            