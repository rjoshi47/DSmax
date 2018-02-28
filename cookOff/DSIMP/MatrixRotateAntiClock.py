'''
Created on 04-Nov-2017

@author: rjoshi
'''

def rotateAnti90(mat, m, n):
    temp = [[0 for i in range(0,n)] for j in range(0, m)]
    for i in range(0, m):
        for j in range(0, n):
            temp[i][j] = mat[i][j]
            
    for i in range(0, m):
        for j in range(0, n):
            mat[i][j] = temp[j][(n-1)-i]
    
def printMat(mat, m, n):
    print()
    for i in range(0, m):
        for j in range(0, n):
            print(mat[i][j], end=" ")
        print() 
    
(m, n) = (4,4)
mat = [[0 for i in range(0,n)] for j in range(0, m)]
for i in range(0, m):
        for j in range(0, n):
            mat[i][j] = i+j
printMat(mat, m, n)

rotateAnti90(mat, m, n)

printMat(mat, m, n)