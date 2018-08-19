'''
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
We are creating two maps here map2 makes sure that we get length 2 GP and map3 gives us 3 length GP.

For a entry v in array if it is not in map3 or map2 we multiply the number with factor k and put in map2
- Here we are predicting that next value in GP should be v*k
If v is in map2 then we add v*k in map3
- Here we predict that next value in GP should be v*k and if found will make sure that it is a 3 length GP.

'''
(n,k) = input().split(" ")
n = int(n)
k = int(k)
nums = list(map(int, input().split(" ")))

map2 = {}
map3 = {}
count = 0

for i in range(n):
    v = nums[i]
    if v in map3:
        count += map3[v]
    if v in map2:
        if v*k in map3:
            map3[v*k] += map2[v]
        else:
            map3[v*k] = map2[v]
    
    if v*k not in map2:
        map2[v*k] = 1
    else:
        map2[v*k] += 1

print(count)
