'''
https://www.hackerrank.com/challenges/minimum-swaps-2?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Idea is to swap the element at each index to its correct position till we get element for this index.
We do this for each index where wrong element is present.
'''

def findSwaps(nums):
    nums = [0]+nums
    swaps = 0
    
    k = 1
    while k < len(nums):
        if k == nums[k]:
            k += 1
        else:
            while k != nums[k]:
                v = nums[k]
                nums[k], nums[v] = nums[v], nums[k]
                swaps += 1
    
    return swaps

n = input()
print(findSwaps(list(map(int, input().split(" ")))))
