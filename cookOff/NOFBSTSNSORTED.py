'''
Created on 19-Mar-2017

@author: rjoshi
'''
myDict = {}
myDict[0] = 1
myDict[1] = 1
    
def generateGroups(n):
    global myDict
    for j in range(2, n+1):
        k = j - 1
        gSum = 0
        for i in range(0, j):
            gSum = gSum + int(myDict[i]) * int(myDict[k - i])
        myDict[j] = gSum
    return myDict[n]

print(generateGroups(1))        
print(generateGroups(2))
print(generateGroups(3))
print(generateGroups(4))
print(generateGroups(5))
print(generateGroups(6))
print(generateGroups(7))
print(generateGroups(8))