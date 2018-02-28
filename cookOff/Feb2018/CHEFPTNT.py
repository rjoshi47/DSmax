'''
Created on 03-Feb-2018

@author: rjoshi
'''
res = []
for ww in range(int(input())):
    nums = input().split(" ")
    days = input()
    
    eoDict = {}
    eoDict[0] = 0
    eoDict[1] = 0
    k = int(nums[3])
    
    for j in range(0, k):
        if days[j] == 'E':
            eoDict[0] += 1
        else:
            eoDict[1] += 1
    
    target = int(nums[0])
    months = int(nums[1])
    factor = int(nums[2])
    
    completed = 0
    odays = int(months/2)
    edays = int(months/2)

    if months % 2 != 0:
        odays += 1
    
    oddAvailableBW = min(odays*factor, eoDict[1])
    eddAvailableBW = min(edays*factor, eoDict[0])
    
    if oddAvailableBW + eddAvailableBW >= target:
        res.append("yes")
    else:
        res.append("no")

for xx in res:
    print(xx)