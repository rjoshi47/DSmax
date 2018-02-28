'''
Created on 16-Jul-2017

@author: rjoshi
'''    
def getDay(lday, fd):
    h = len(lday)-1
    l = 0
    if fd > lday[-1]:
        return -1
    while l <= h:
        m = int((l+h)/2)
        if lday[m] < fd:
            l = m+1
        else:
            ans = m
            h = m - 1
    return ans
res = []
tests = int(input())
for i in range(0, tests):
    tSum = 0
    sumSad = 0
    (t, days) = input().split(" ")
    nlist = []
    for v in range(0, int(t)):
        nums = list(map(int, input().split(" ")))
        nlist.append(nums)
        sTime = nums[0]
        count = nums[1]
        cost = nums[2]
        tSum = tSum + count*cost
        
    days = int(days)
    vis = [0]*int(days+1)
    vcount = 0
    timeDict = {}
    notSad = 0
    ldays = []
    for d in range(0, days):
        ldays.append(d+1)
    nlist.sort(key=lambda x:x[2], reverse=True)
    for i in range(0, len(nlist)):
        (sTime, count, cost) = nlist[i]
        if len(ldays) == 0:
            continue
        dayi = getDay(ldays, sTime)
        if dayi == -1:
            continue
        if dayi + count - 1 < len(ldays):
            del ldays[dayi: dayi + count]
#             for u in range(dayi, dayi + count):
#                 del ldays[dayi]
            notSad = notSad + count*cost
        else:
            cc = 0
            cc = len(ldays) - dayi
            del ldays[dayi: len(ldays)]
#             for u in range(dayi, len(ldays)):
#                 del ldays[dayi]
                
            notSad = notSad + cc*cost
        
    res.append(tSum - notSad)

for cc in res:
    print(cc)    
