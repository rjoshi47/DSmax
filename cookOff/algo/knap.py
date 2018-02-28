'''
Created on 04-Jun-2017

@author: rjoshi
'''
coins = []
coinCount = 0
came_from = {}
flag =True
def getPath(camefrom, i, j):
    
    path = []
    path.append((i,j))
    while (i,j) in camefrom:
        (i, j) = camefrom[(i,j)]
        path.append((i,j))
    path.reverse()
    
    px = -1
    for (i,j) in path:
        if px != i:
            if j < len(coins) and coins[j] != 0:
                print(coins[j], end=" ")
        px = i
    print("#####")
    
def getMaxVal(knap, i, j, v):
    global flag
    #print(i,j)
    val1 = knap[i][j+1]
    val2 = 0
    if i - coins[j] >= 0:
        val2 = knap[i - coins[j]][j+1] + coins[j]
        
    if val1 >= val2:
        came_from[(i,j)] = (i,j+1)
    else:
        came_from[(i,j)] = (i - coins[j],j+1)
    
    if val2 == v and flag:
        getPath(came_from, i, j)
        flag = False
    return max(val1, val2)

def buildKnapSack(w, h, v):
    knap = [[0 for x in range(w)] for y in range(h)]
    for i in range(w-2, -1, -1):
        for j in range(0, h):
            knap[j][i] = getMaxVal(knap, j, i,v)
    coins.append(0)
    print(coins)
    for i in range(0, h):
        for j in range(0, w):
            print(knap[i][j], end=", ")
        print()
       
(n, v) = input().split(" ")
for i in range(0, int(n)):
    (c, q) = input().split(" ")
    for k in range(0, int(q)):
        coins.append(int(c))
        coinCount = coinCount + 1
buildKnapSack(coinCount + 1, int(v)+1, int(v))