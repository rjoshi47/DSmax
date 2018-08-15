'''
sherlock and anagrams
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
Here, we are generating all contigous substrings of a string and storing them in map in sorted order.
Now, based on count of a string key in our map we can mae nC2 combinations out of it.
'''

def subSets(nums, mDict):
    n = len(nums)
    for i in range(n):
        s = ''
        for j in range(i, n):
            s += nums[j]
            sortStr = ''.join(sorted(s))
            if sortStr not in mDict:
                mDict[sortStr] = 1
            else:
                mDict[sortStr] += 1
            #print(''.join(sorted(s)))

res = []       
for _ in range(int(input())):
    mstr = input()
    mDict = {}
    subSets(mstr, mDict)
    
    c = 0
    for (k, v) in mDict.items():
        c += int((v*(v-1))/2)
    res.append(c)
    
for xx in res:
    print(xx)    
