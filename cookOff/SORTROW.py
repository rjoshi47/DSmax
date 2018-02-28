'''
Created on 08-Mar-2017

@author: rjoshi
'''
def swap(nums, one, two):
    temp = nums[one]
    nums[1] = nums[2]
    nums[2] = temp
    
def cycleSort(nums, n):
    for start in range(0, n-1):
        item = nums[start]
        pos = start
        for i in range(start + 1, n):
            if nums[i] < item:
                pos = pos + 1
        
        if pos == start:
            continue
        
        while item == nums[pos]:
            pos = pos + 1
#         temp = nums[pos]
#         nums[pos] = item
#         nums[start] = temp
        temp = nums[pos]
        nums[pos] = item
        item = temp
     
        while pos != start:
            pos = start
            for i in range(start + 1, n):
                if nums[i] < item:
                    pos = pos + 1
         
            while item == nums[pos]:
                pos = pos + 1
            temp = nums[pos]
            nums[pos] = item
            item = temp

nums = [2, 8,12,14,1,5,7,10,16,13,6,4,3,9,11,15]
cycleSort(nums, len(nums))
print(nums)