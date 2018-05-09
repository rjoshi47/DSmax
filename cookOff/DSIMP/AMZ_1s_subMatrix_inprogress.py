'''
Created on May 9, 2018

@author: devuser

'''

res = []

def inBound(r, c, idx):
    (x, y) = idx
    return 0 <= x < r and 0 <= y < c

def padosi(r,c,idx):
    (x,y) = idx
    padosi = [(x,y+1), (x+1,y), (x+1, y+1)]
    return filter(inBound, padosi)

def processMat(mat):
    

for _ in range(int(input())):
    (r, c) = input().split(" ")
    tnums = input()
    nums = []
    for k in range(len(tnums)):
        if len(tnums[k]) > 0:
            nums.append(int(tnums[k]))
            
    mat = [[0 for i in range(0,c)] for j in range(0,r)]
    k = 0
    for i in range(0, r):
        for j in range(0, c):
            mat[i][j] = nums[k]
            k += 1
