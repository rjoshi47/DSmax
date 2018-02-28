'''
Created on 22-Oct-2017
http://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
@author: rjoshi
'''

def getLongestSpanSameSum(arr1, arr2):
    # arrays have same size
    n = len(arr1)
    
    sumArr1 = 0
    sumArr2 = 0
    
    maxLen = 0
    diffDict = {}
    
    for i in range(0, n):
        sumArr1 += arr1[i]
        sumArr2 += arr2[i]
        
        diff = sumArr2 - sumArr1
        
        if diff == 0:
            maxLen = i + 1
        elif diff not in diffDict:
            diffDict[diff] = i
        else:
            maxLen = max(maxLen, i - diffDict[diff])
    
    print(maxLen)
    
arr1 = [0, 1, 0, 0, 0, 0]
arr2 = [1, 0, 1, 0, 0, 1]

# arr1 = [0, 1, 0, 1, 1, 0, 1]
# arr2 = [0, 1, 0, 1, 1, 0, 1]
# 
# arr1 = [0, 0, 0, 0, 0, 1, 0]
# arr2 = [1, 0, 1, 0, 0, 0, 0]

getLongestSpanSameSum(arr1, arr2)
                
                
                
                
                