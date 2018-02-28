'''
Created on 11-Jan-2018

@author: rjoshi
'''
def find3Numbers(A, s, e,sum, nums):
    for i in range(s,e):
        for j in range(i+1, e+1): 
            for k in range(j + 1, e+1):
                if A[i] + A[j] + A[k] == sum:
                    nums[0] = i
                    nums[1] = j
                    nums[2] = k
                    return True
    return False

def getPair(arr, s, e, n):
    nDict = {}
    for i in range(s, e+1):
        if arr[i] == n:
            return (-1, i)
        elif n - arr[i] in nDict:
            return (i, nDict[n-arr[i]])
        else:
            nDict[arr[i]] = i
    return (-1, -1)  

def subSum(w, s, k, r, x, m, x1, n):
    msum = 0
    lp = 0
    for i in range(0, len(x)):
        msum += w[i]
        x[i] = 1
        lp = i
        if msum >= m:
            break
    extra = msum - m
    f = 0
    if extra > 0 and extra != x1:
        for i in range(0, lp+1):
            if extra == w[i]:
                x[i] = 0
                f = 1
                break
    elif extra !=0 and extra == x1 :
        if lp+1 < len(x):
            msum = msum - w[lp]
            x[lp] = 0
            msum = msum + w[lp+1]
            x[lp+1] = 1
            extra = msum - m
            f = 0
            for i in range(0, lp):
                if extra == w[i]:
                    x[i] = 0
                    f = 1
                    break
            if f == 0 and extra == w[lp]:
                if w[lp] == w[lp-1] + w[0]:           
                    x[lp-1] = 0
                    x[0] = 0
                    x[lp] = 1
                elif w[lp] == w[lp-1] + w[1]:
                    x[lp-1] = 0
                    x[1] = 0
                    #x[lp] = 1
                        
            

res = []
tests = int(input())
for zz in range(0, tests):
    (x1, n) = input().split(" ")
    x1 = int(x1)
    n = int(n)
    
    w = [0]*(n-1)
    w[0] = 1     
    if x1 == 1:
        w[0] = 2  
    for k in range(1, n-1):
        if x1 != 1 and k == x1-1:
            w[k] = w[k-1] + 2
        else:
            w[k] = w[k-1] + 1
    
    #print(w)
    msum = int((n*(n+1))/2)
    msum -= x1
    if msum % 2 != 0:
        res.append("impossible")
    else:
        x = [0]*(n-1)
        subSum(w, 0, 0, msum, x, int(msum/2), x1, n)
        fsum = 0
        for i in range(0, (n-1)):
            if x[i] == 1:
                fsum += w[i]
        if fsum != int(msum/2):
            res.append("impossible")
        else:
            fans = ''
            for i in range(0, (n-1)):
                if i == x1 - 1:
                    fans += '2'
                if x[i] == 1:
                    fans += '1'
                else:
                    fans += '0'
            if x1 - 1 == n-1:
                fans += '2'
            res.append(fans)
    
for ii in res:
    print(ii)

