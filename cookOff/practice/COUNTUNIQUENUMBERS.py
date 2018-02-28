'''
Created on 18-May-2017

@author: rjoshi
'''
def getUniqueCount(myString, s , e, myDict):
    if s > e:
        return
    if myString[s] == myString[e]:
        if myString[s] not in myDict:
            myDict[myString[s]] = e - s + 1
        else:
            myDict[myString[s]] = myDict[myString[s]] + e - s + 1
        return
    mid = int((s + e)/2)
    getUniqueCount(myString, s , mid, myDict)
    getUniqueCount(myString, mid+1 , e, myDict)

myDict = {} 
myStr = "aazzbbcccddeefxx"
getUniqueCount(myStr, 0 , len(myStr)-1, myDict)
print(myDict)