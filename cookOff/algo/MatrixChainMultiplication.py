'''
Created on 10-Sep-2017

@author: rjoshi
M[i][j] = min{ M[i][k] + M[k+1][j] + P(i-1)P(k)P(j) } for i <=k < j
'''
A = ['0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6']
#P = [30, 35, 15, 5, 10, 20, 25]
P = [30, 35, 15, 5, 10, 20, 25]
M = [[0]*len(P) for y in range(len(P))]
S = [[0]*len(P) for y in range(len(P))]

# Traverse diagonally [1,2] [2,3] [3,4] ...
for i in range(1, len(P)):
    for j in range(1, len(P)-i):
        vmin = 1000000
        for k in range(j, j+i):
            print((j,j+i), end=" ")
            mv = M[j][k] + M[k+1][j+i] + P[j-1]*P[k]*P[j+i]
            if mv < vmin:
                vmin = mv
                S[j][j+i] = k
        M[j][j+i] = vmin
        print(" ")
        
for i in range(1, len(P)):
    for j in range(1, len(P)):
        print(M[i][j], end=" ")
    print()
    
for i in range(1, len(P)):
    for j in range(1, len(P)):
        print(S[i][j], end=" ")
    print()

def getMutiplySeq(i,j):
    if i == j:
        return A[i]
    else:
        k = S[i][j]
        x = getMutiplySeq(i,k)
        y = getMutiplySeq(k+1,j)
        return '('+x+','+y+')'
    
print(getMutiplySeq(1, 6))