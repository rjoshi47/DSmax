'''
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec03.pdf
The idea is to keep array till k in insertioSort sorted, as in the original osrted array.
Start from k = 1 and find its position in already sorted array nums[0, k-1].
The shift elements and store kth element at the position found using binary search.
'''
def findPos(nums, num, s, e):
    if s == e:
        if num <= nums[s]:
            return s
        else:
            return s + 1
    else:
        mid = int((s+e)/2)
        if num <= nums[mid]:
            return findPos(nums, num, s, mid)
        else:
            return findPos(nums, num, mid+1, e)

def shiftNums(nums, ele, pos, k):
    for i in range(k, pos, -1):
        nums[i] = nums[i-1]
    nums[pos] = ele
    
def insertionSort(nums):
    for k in range(1, len(nums)):
        pos = findPos(nums, nums[k], 0, k-1)
        if k != pos:
            shiftNums(nums, nums[k], pos, k)
            print(nums)
        
insertionSort([4,3,1,2])
