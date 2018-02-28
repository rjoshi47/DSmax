'''
Created on 15-Oct-2017

@author: rjoshi
'''

def partition(arr, l, r, idx):
    piv = idx
    while l < r:
        if arr[l] > piv and arr[r] < piv:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif arr[l] > piv and arr[r] >= piv:
            r -= 1
        elif arr[l] < piv and arr[r] < piv:
            l += 1
        else:
            l += 1
            r -= 1
    arr[l], arr[idx] = arr[idx], arr[l]
    return l

def getMedianIndex(arr):
    al = len(arr)
    idx = int(al/2)
    if al % 2 != 0:
        idx = idx + 1
    visited = [0]*len(arr)
    for i in range(0, idx):
        minIdx = -1
        for j in range(0, al):
            if visited[j] == 0 and minIdx == -1:
                minIdx = j
            if visited[j] == 0 and arr[j] < arr[minIdx]:
                minIdx = j
        visited[minIdx] = 1
    return minIdx 

def getMedian(arr):
    medians = []
    s = 0
    while s < len(arr):
        medianIdx = getMedianIndex(arr[s:s+5])
        medians.append(arr[medianIdx + s])
        s = s + 5
    return medians
    

def getRank(arr, l , r,  k):
    medians = getMedian(arr)
    medianVal = getRank(medians, int(len(medians)/2))
    med = partition(arr, 0, len(arr)-1, medianVal)
    if med == k:
        return arr[med]
    elif med > k:
        return getRank(arr, int(len(medians)/2))
    print(medians)
arr = [1, 9, 4, 11, 8, 3, 2, 6, 15, 7, 10, 5, 13, 18, 12, 16, 14, 17]
getRank(arr, 3)
#getMedian(arr[15:15+5], 0, min(4,len(arr)-1-15))
#getMedianIndex(arr[15:20])
