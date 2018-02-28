'''
Created on 08-Oct-2017

@author: rjoshi
'''

def getBitonicSeq(arr):
    pSign = ''
    count = 1
    seqLen = 0
    pEle = arr[0]
    si = sif = 0
    eif = 0
    if len(arr) > 1:
        for i in range(1, len(arr)):
            sign = arr[i] - pEle 
            pEle = arr[i]
            if pSign == '':
                if sign > 0:
                    pSign = '+'
                else:
                    pSign = '-'
                count += 1
            elif pSign == '+':
                if sign < 0:
                    pSign = '-'
                count += 1
            elif pSign == '-':
                if sign > 0:
                    if seqLen < count:
                        seqLen = count
                        sif = si
                        eif = i - 1
                    pSign = '+'
                    count = 2
                    si = i - 1
                else:
                    count +=1
                    
    if seqLen < count:
        seqLen = count
        sif = si
        eif = len(arr)
    return arr[sif:eif+1]

print(getBitonicSeq([40, 30, 2, 10, 100, 200, 300, 400,500, 600, 700, 4000, 2, 1, 2,3,4,5,6,7,8,9,10,11,1,10]))
                