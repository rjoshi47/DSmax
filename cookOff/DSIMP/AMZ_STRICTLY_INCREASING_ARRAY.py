'''
Created on Dec 10, 2019
https://practice.geeksforgeeks.org/problems/convert-to-strictly-increasing-array/0
@author: rj250201
'''

def get_just_greater(nums, a):
    ng = 1000000
    ngi = len(nums) - 1
    for i in range(len(nums)):
        if nums[i] > a:
            if nums[i] < ng:
                ng = nums[i]
                ngi = i
    return ngi

def LIS(nums):
    l_nums = []
    for i in range(len(nums)):
        l_nums.append(nums[i])
        
        ngi = get_just_greater(l_nums, nums[i])
        
        if ngi != len(l_nums) - 1:
            l_nums.remove(l_nums[ngi])
    return len(l_nums)

res = []
for _ in range(int(input())):
    n = input()
    nums = list(map(int, input().strip().split(" ")))
    # This is to neutralize the make sure in LCS we have j - i >= nums[j] - nums[i] 
    # for 1 2 3 7 4 => 1 1 1 4 0 ????????????????
    for i in range(len(nums)):
        nums[i] = nums[i] - i
    res.append(len(nums) - LIS(nums))
    
for xx in res:
    print(xx)
    
