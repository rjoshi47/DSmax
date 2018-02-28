'''
Created on 27-May-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    n = int(input())
    nums = input().split(" ")
    if n % 2 != 0:
        if n == 1:
            if int(nums[0]) != 1:
                results.append(0)
            else:
                results.append(int(nums[0])-1)
        else:
            mid = int(n/2)
            val = mid + 1
            count = 0
            if val != int(nums[val-1]):
                count = count + abs(val - int(nums[val-1]))
            v = 1
            for k in range(mid-1, -1, -1):
                val = val - 1
                if val != int(nums[k]):
                    count = count + abs(val - int(nums[k]))
                if val != int(nums[mid+v]):
                    count = count + abs(val - int(nums[mid+v]))
                v = v + 1
            results.append(count)
    else:
        count = 0
        if n == 2:
            if int(nums[0]) != 1:
                count = count + int(nums[0]) - 1
            if int(nums[1]) != 1:
                count = count + int(nums[1]) - 1
            results.append(count)
        else:
            mid = int(n/2) - 1
            val = mid + 1
            v = 1
            for k in range(mid,-1,-1):
                if val != int(nums[k]):
                    count = count + abs(val - int(nums[k]))
                if val != int(nums[mid+v]):
                    count = count + abs(val - int(nums[mid+v]))
                val = val - 1
                v = v + 1
            results.append(count)        
            
for xx in results:
    print(xx)
     

