'''
Created on 28-May-2017

@author: rjoshi
'''
import math
seg_tree = []

def makeTree(nums, s_i, e_i, t_i):
    global seg_tree
    st = seg_tree
    if s_i == e_i:
        st[t_i] = int(nums[s_i])
        return st[t_i]
    mid = s_i + (e_i - s_i) // 2
    st[t_i] = makeTree(nums, s_i, mid, 2 * t_i + 1) + makeTree(nums, mid + 1, e_i, 2 * t_i + 2)
    return st[t_i]

def segTree(nums):
    global seg_tree
    if nums:
        tree_length = 2 * (2 ** int(math.ceil(math.log(len(nums), 2)))) - 1
        seg_tree = [0] * tree_length
        makeTree(nums, 0, len(nums) - 1, 0)

def sumRange(nums, i, j):
    global seg_tree
    def sumRange_until(s_i, e_i, t_i):
        if i <= s_i and j >= e_i:
            return st[t_i]
        if s_i > j or e_i < i:
            return 0
        mid = s_i + (e_i - s_i) // 2
        return sumRange_until(s_i, mid, 2 * t_i + 1) + sumRange_until(mid + 1, e_i, 2 * t_i + 2)

    st = seg_tree
    if i == j:
        return int(nums[i])

    return sumRange_until(0, len(nums) - 1, 0)

def getEsum(n):
    m = int(n/2)
    sum = int((m*(m+1))/2)
    return 2*sum + m + 1

results = []
tests = int(input())
for i in range(0, tests):
    n = int(input())
    nums = input().split(" ")
    #global seg_tree
    seg_tree = []
    segTree(nums)
    gSum = 0
    for i in range(0, n):
        gSum = gSum + int(nums[i])
    
    diff = -1
    k = 0
    for i in range(0, n):
        for j in range(0,n,2):
            mSum = sumRange(nums, i, j)
            mdiff = abs(getEsum(abs(j-i) + 1) - mSum) + (gSum - mSum)
            if diff == -1:
                diff = mdiff
            elif mdiff < diff:
                #print(i,j)
                diff = mdiff
    
    results.append(diff)

for xx in results:
    print(xx)
        
# segTree(['1','2','3','4','5','6'])
# print(seg_tree)
# print(sumRange(['1','2','3','4','5','6'],0,3))
# print(sumRange(['1','2','3','4','5','6'],2,3))
# print(sumRange(['1','2','3','4','5','6'],3,3))
# print(sumRange(['1','2','3','4','5','6'],3,5))