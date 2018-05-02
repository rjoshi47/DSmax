'''
Created on 02-May-2018

@author: rjoshi
'''
import heapq
class Code:
    def __init__(self):
        self.val = 0
        self.right = None
        self.left = None
        self.leftCode = 0
        self.rightCode = 1
        
res = []
for _ in range(0, int(input())):
    mstr = input().strip()
    tnums = input().split(" ")
    
    nums = []
    for k in range(0, len(tnums)):
        if len(tnums[k]) > 0:
            heapq.heappush(nums, (int(tnums[k]), mstr[k]))
            
    codeRoot = None
    while len(nums) != 1:
        code1 = heapq.heappop(nums)
        code2 = heapq.heappop(nums)
        
        codeParent = Code()
        codeParent.val = code1[0] + code2[0]
        codeParent.left = code1
        codeParent.right = code2
        code1.parent = codeParent
        code2.parent = codeParent
        
        codeRoot = codeParent
        
        heapq.heappush(nums, (codeParent.val, codeParent))
        
    
    
