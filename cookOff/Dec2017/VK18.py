'''
Created on 09-Dec-2017

@author: rjoshi
''' 
 
#tests = int(input())  
N = 10
val = [0]*(2*N+7)
ans = [0]*(N+7)

results = []  
def getSum(msum): 
    sE = 0 
    sO = 0 
    msum = int(msum)
    while True:
        if msum > 0:
            v1 = msum%10
            if v1 % 2 == 0:  
                sE += v1  
            else:  
                sO += v1
            msum = int((msum - v1)/10)
        else:
            break
    return abs(sE - sO) 
 
def preProcess():
    val[1] = 0
    for i in range(2, N+N+1):
        val[i] = val[i-1] + getSum(i)
        
    ans[1] = 2
    for i in range(2, N):
        ans[i] = ans[i - 1] + (2 * (val[2 * i] - val[i])) -  (val[2 * i] - val[2 * i - 1])
    print(val)
    print(ans)
    
preProcess()