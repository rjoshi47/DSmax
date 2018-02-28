'''
Created on 09-Dec-2017

@author: rjoshi
''' 
 
tests = int(input())  
 
results = []  
 
def getSum(msum): 
    return abs(sum(i * ((i % 2) * 2 - 1) for i in map(int, str(msum))))
#     sE = 0 
#     sO = 0 
#     msum = int(msum)
#     while True:
#         if msum > 0:
#             v1 = msum%10
#             if v1 % 2 == 0:  
#                 sE += v1  
#             else:  
#                 sO += v1
#             msum = int((msum - v1)/10)
#         else:
#             break
#     return abs(sE - sO) 
 
#print(getSum(12344)) 
 
for z in range(0, tests):  
    n = int(input())   
    arr = []  
    farr = []
    ssum = 0
    
    if n == 1:
        results.append(2)
        continue
    
    for i in range(1, n+1):
        v = getSum(i+1)
        ssum += v
        farr.append(v)
    
    larr = []
    dsum = 0
    s = n+n
    li = 0
    
    for i in range(n+2, n+n+1):
        v = getSum(i)
        dsum += v
        larr.append(v)
    
    odsum = dsum
    ossum = ssum
    subssum = 0
    sublsum = 0
    for i in range(0, len(larr)-1):
        subssum += farr[i]
        sublsum += larr[len(larr)-(i+1)]
        ssum += (ossum - subssum)
        dsum += (odsum - sublsum)
        
#     print(ssum)
#     print(dsum)
#     
#         
#     print(len(farr))
#     print(len(larr))
#     print(" $$$$$$$$$$ ")
    results.append(ssum + farr[len(farr)-1] + dsum)
    
for xx in results:
    print(xx)