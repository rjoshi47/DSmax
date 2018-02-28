'''
Created on 17-Oct-2017
http://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/

@author: rjoshi
'''

def getSumPath(arrN, arrM):
    n = len(arrN)
    m = len(arrM)
    
    i = j = sumN = sumM = result = 0
    
    while i < n and j < m:
        if arrN[i] < arrM[j]:
            sumN += arrN[i]
            i += 1
        elif arrN[i] > arrM[j]:
            sumM += arrM[j]
            j += 1
        else:
            result += max(sumN, sumM)
            sumN = sumM = 0
            
            while i < n and j < m and arrN[i] == arrM[j]:
                result += arrN[i]
                i += 1
                j +=1
    
    while i < n:
        sumN += arrN[i]
        i += 1
        
    while j < m:
        sumM += arrM[j]
        j +=1
        
    return result + max(sumN, sumM)

print(getSumPath([2, 3, 7, 10, 12, 15, 30, 34], [1, 5, 7, 8, 10, 15, 16, 19]))