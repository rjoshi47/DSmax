'''
Created on 20-May-2018

@author: rjoshi
g0 - numbers with remainder 0
g1 - numbers with remainder 1
g2 - numbers with remainder 2

all pairs of 2 and 3 div by 3 are
 = (pair of 2 numbers in g0 + pair of 3 numbers in g0) # as all numbers are already div by 3
+ (pair of 3 numbers in g1) # remainder is 1 so 3 number pair will be div by 3
+ (pair of 3 number in g2)  # remainder is 2 so 3 number pair will be div by 3
+ (g1*g2) # select 1 from g1 and 1 from g2 to for 2 number pair
+ g0*(g1*g2) # any g0 number can be added to above 2 number pair to make 3 number pair

overall formula = (g0C2 + g0C3) + (g1C3 + g2C3) + (1+g0)*(g1*g2) # C represents combination

'''
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def getGroups(g0, g1, g2):
    pairs = 0
    if g0 >= 2:
        pairs += nCr(g0, 2)
    if g0 >= 3:
        pairs += nCr(g0, 3)
    if g1 >= 3:
        pairs += nCr(g1, 3)
    if g2 >= 3:
        pairs += nCr(g2, 3)
    
    if g1 > 0 and g2 > 0:
        pairs += (1+g0)*(g1*g2)
        
    return int(pairs)

res = []
for _ in range(0, int(input())):
    n = int(input())
    tnums = input().split(" ")
    nums = []
    for k in range(0, len(tnums)):
        if len(tnums[k]) > 0:
            nums.append(int(tnums[k]))
            
    g0 = 0
    g1 = 0
    g2 = 0
    
    for k in range(0, n):
        if nums[k] % 3 == 0:
            g0 += 1
        elif nums[k] % 3 == 1:
            g1 += 1
        elif nums[k] % 3 == 2:
            g2 += 1
            
    res.append(getGroups(g0, g1, g2))

for xx in res:
    print(xx)
