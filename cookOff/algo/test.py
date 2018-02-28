'''
Created on 03-Dec-2017

@author: rjoshi
'''
print(2^7)

def getBits(num):
    count = 0
    while num > 0:
        count += 1&num
        num = num >> 1
    return count

def maxSum(nums):
    ms = 0
    mt = 0
    for i in range(0, len(nums)):
        ms = ms + nums[i]
        if ms > mt:
            mt = ms
        if ms < 0:
            ms = 0
    print(mt)
maxSum([-1, -12, -1, 3, 0, -1, -1, 12, -11, 11, -14])

print(getBits(2^7))

        
        