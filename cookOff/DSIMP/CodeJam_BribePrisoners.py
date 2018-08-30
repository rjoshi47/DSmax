'''
Bribe the Prisoners
https://code.google.com/codejam/contest/189252/dashboard#s=p2
'''
#prisonDict = {}
def solve(releaseCells, l, r):
    if (l,r) in prisonDict:
        return prisonDict[(l,r)]
    
    minCoins = 0
    for i in range(len(releaseCells)):
        if releaseCells[i] >= l and releaseCells[i] <= r:
            coins = ((r-l) + solve(releaseCells, l, releaseCells[i]-1) 
                     + solve(releaseCells, releaseCells[i]+1,r))
            if minCoins == 0:
                minCoins = coins
            else:
                minCoins = min(minCoins, coins)
    
    prisonDict[(l,r)] = minCoins
    return minCoins

#solve([5,7,9], 1, 11)
#print(prisonDict[(1,11)])
res = []
for _ in range(int(input())):
    (n, p) = input().split(" ")
    releaseCells = list(map(int, input().split(" ")))
    global prisonDict
    prisonDict = {}
    solve(releaseCells, 1, int(n))
    res.append(prisonDict[(1, int(n))])

i = 1
for xx in res:
    print("Case #"+str(i)+": "+str(xx))
    i += 1
