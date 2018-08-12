'''
https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
Initially whole array is 0s.
Then for given l,r,v increment values by v from l to r
Finally output max element in array

012 345 678
000 000 000
010 000 0-10 after (1,6,1)  -> See if we add elements -> 011 111 100 -> max 1
010 020 0-1-2 after (3,7,2) -> 011 133 320 -> max3

'''
(n, k) = input().split(" ")
nums = [0]*int(n)
for i in range(int(k)):
    ops = list(map(int, input().split(" ")))
    nums[ops[0]-1] += ops[2]
    if ops[1] < int(n):
        nums[ops[1]] -= ops[2]
    
maxV = 0
val = 0
for v in range(int(n)):
    val += int(nums[v])
    maxV = max(maxV, val)
    
print(maxV)
