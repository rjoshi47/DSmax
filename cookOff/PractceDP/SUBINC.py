'''
Created on 27-Jan-2018

@author: rjoshi
'''
def getNonDec(nums):
    arr = [1]*len(nums)
    
    for i in range(1, len(nums)):
        if int(nums[i]) >= int(nums[i-1]):
            arr[i] = arr[i-1] + 1
    
    msum = 0
    for i in range(0, len(arr)):
        msum += arr[i]
    
    #print(arr)
    return msum        

res = []
for ll in range(0, int(input())):
    nn = input()
    nums = input().split(" ")
    res.append(getNonDec(nums))
        
for xx in res:
    print(xx)