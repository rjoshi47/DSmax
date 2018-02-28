'''
Created on 07-Jan-2018

@author: rjoshi
'''

LCS = [[0]*5000 for y in range(5000)]

def findLenOfLCS(str1, str2):
    str1 = '0' + str1
    str2 = '0' + str2
    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            if str1[j] == str2[i]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    return LCS[len(str2)-1][len(str1)-1]
   
res = []
tests = int(input())
for z in range(0, tests):
    (n, m) = input().split(" ")
    aArr = input()
    bArr = input()
    
    arr1 = ''
    i = 0
    while i < len(aArr):
        c = aArr[i]
        j = i+1
        while j < len(aArr) and aArr[j] == c:
            i += 1
            j += 1
        i += 1
        arr1 += c
    
    arr2 = ''
    i = 0
    while i < len(bArr):
        c = bArr[i]
        j = i + 1
        while j < len(bArr) and c == bArr[j]:
            i += 1
            j += 1
        i += 1
        arr2 += c
    
    
    lcsLen = findLenOfLCS(arr1, arr2)
    res.append(len(arr2) + len(arr1) - lcsLen )
        
for xx in res:
    print(xx)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            