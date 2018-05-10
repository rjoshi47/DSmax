'''
Created on 09-May-2018

@author: rjoshi

0 1 0 1 0 1 
1 0 1 0 1 0 
0 1 1 1 1 0 
0 0 1 1 1 0 
1 1 1 1 1 1


'''

res = []
for _ in range(int(input())):
    (r, c) = input().split(" ")
    r = int(r)
    c = int(c)
    tnums = input().split(" ")
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
    
    suMat = [[0 for i in range(0,c)] for j in range(0,r)]
    for i in range(0, r):
        suMat[i][0] = mat[i][0]
    for j in range(0,c):    
        suMat[0][j] = mat[0][j]
        
    maxV = 1
    for i in range(1, r):
        for j in range(1, c):
            if mat[i][j] == 1:
                suMat[i][j] = min(suMat[i-1][j-1], suMat[i-1][j], suMat[i][j-1]) + 1
                maxV = max(maxV, suMat[i][j])
    
    #print(suMat)
    res.append(maxV)
    
for xx in res:
    print(xx)
