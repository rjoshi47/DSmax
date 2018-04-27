'''
Created on Apr 27, 2018

@author: devuser
for n = 2, 43
00 -> ()
01 -> (3)
10 -> (4)
11 -> (4 3) -> sort -> (3 4)

output: ()(3)(4)(3 4)
'''
from operator import itemgetter
def printPowerSet(nums, n):
    setSize = pow(2, n)
    strArr = []
    
    arrDict = {}
    for c in range(0, setSize):
        tStr = []
        for j in range(0, n):
            if c & 1 << j:
                tStr.append(nums[j])
        tStr.sort()
        mstr = " ".join(tStr)
        if mstr not in arrDict:
            strArr.append(('('+mstr+')', mstr))
            arrDict[mstr] = 1
            
    strArr.sort(key=itemgetter(1))
    return strArr

res = []
for _ in range(0, int(input())):
    n = int(input())
    nums = input().split(" ")
    farr = printPowerSet(nums, n)
    vStr = ''
    for (a, b) in farr:
        vStr += a
    res.append(vStr)
    
for xx in res:
    print(xx)
