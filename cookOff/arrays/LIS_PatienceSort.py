'''
Created on 10-Oct-2017
33.3  Patience sorting: a model
http://web.mit.edu/18.338/www/2012s/handouts/LIS.pdf
@author: rjoshi
'''

def getPileImpl(arr, num, s, e):
    if s == e:
        return s
    else:
        m = int((s+e)/2)
        if m == s:
            if arr[m] > num:
                return m
            elif arr[m+1] > num:
                return m+1 
        elif arr[m] > num and arr[m-1] < num:
            return m
        elif arr[m] > num and arr[m-1] > num:
            return getPileImpl(arr, num, s, m)
        elif arr[m] < num and arr[m+1] > num:
            return m + 1
        elif arr[m] < num and arr[m+1] < num:
            return getPileImpl(arr, num, m+1, e)
        
def getPileIndex(arr, num):
    if len(arr) == 0 or arr[len(arr)-1] < num:
        return -1
    return getPileImpl(arr, num, 0, len(arr)-1)

def LIS(arr):
    goto = [-1]*len(arr)
    pile = []
    pileIdx = []
    for i in range(0, len(arr)):
        idx = getPileIndex(pile, arr[i])
        if idx == -1:
            pile.append(arr[i])
            pileIdx.append(i)
            if len(pileIdx) != 1:
                goto[i] = pileIdx[idx-1]
        else:
            pile[idx] = arr[i]
            pileIdx[idx] = i
            if idx != 0:
                goto[i] = pileIdx[idx-1]
    
    print(pile)
    print(pileIdx)
    print(goto)
    startnum = pileIdx[len(pileIdx)-1]
    print(arr[startnum], end=" ")
    while True:
        idx = goto[startnum]
        if idx == -1:
            break
        print(arr[idx], end=" ")
        startnum = idx
    
arr = [4, 5, 9, 2, 6,  7,8,3,100]
LIS(arr)
    