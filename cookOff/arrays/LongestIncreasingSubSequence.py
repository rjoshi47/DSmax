'''
Created on 08-Oct-2017

@author: rjoshi
'''

def getLongestSubSeqLen(arr):
    seqArr = [1]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        maxSeqLenSoFar = 0
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j] and seqArr[j] > maxSeqLenSoFar:
                maxSeqLenSoFar = seqArr[j]
                
        seqArr[i] = maxSeqLenSoFar + 1
        
    print(seqArr)

def getLongestSubSeq(arr):
    seqArr = [(1, '')]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        maxSeqLenSoFar = 0
        seq = str(arr[i])
        eleIndex = i
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j] and seqArr[j][0] > maxSeqLenSoFar:
                maxSeqLenSoFar = seqArr[j][0]
                eleIndex = j
                
        if eleIndex != i:
            seq = seq +", "+ seqArr[eleIndex][1]
            
        seqArr[i] = (maxSeqLenSoFar + 1, seq)
        
    print(seqArr)
    
arr = [8,30,1,5,2,4,9,7,11]
getLongestSubSeq(arr)
getLongestSubSeqLen(arr)