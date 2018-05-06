'''
Created on 06-May-2018
https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/0
@author: rjoshi
'''
import heapq
class board:
    def __init__(self, size):
        self.size = size
        
    def inBound(self, idx):
        return 0 <= idx <= self.size
    
    def ngBours(self, idx):
        nbs = [idx+1, idx+2, idx+3, idx+4, idx+5, idx+6]
        return filter(self.inBound, nbs)
    
class pQueue():
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    # putting priority as negative so that higher numbers should be considered first
    def put(self, idx):
        heapq.heappush(self.elements, (-idx, idx))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
        
def snakeLadder(n, start, snakeLadderDict):
    graph = board(n)
    frontier = pQueue()
    frontier.put(start)
    costSoFar = {}
    costSoFar[start] = 0
    minCost = 30
    while not frontier.isEmpty():
        current = frontier.get()
        if current == n:
            #print(costSoFar)
            if costSoFar[n] < minCost:
                minCost = costSoFar[n]
        
        for nextPos in graph.ngBours(current):
            newCost = costSoFar[current] + 1
            if nextPos not in costSoFar or costSoFar[nextPos] > newCost:
                costSoFar[nextPos] = newCost
                '''
                If there is a ladder at this position
                we can go directly up without any cost
                '''
                if nextPos in snakeLadderDict:
                    v2 = snakeLadderDict[nextPos]
                    if v2 > nextPos:
                        costSoFar[v2] = newCost 
                        frontier.put(v2)
                frontier.put(nextPos)
    return minCost
    
res = []
for _ in range(0, int(input())):
    n = int(input())
    tnums = input().split(" ")
    nums = []
    for k in range(0, len(tnums)):
        if len(tnums[k]) > 0:
            nums.append(int(tnums[k]))
            
    snakeLadderDict = {}
    for k in range(0, len(nums), 2):
        if k + 1 < len(nums):
            snakeLadderDict[nums[k]] = nums[k+1]
    res.append(snakeLadder(30, 1, snakeLadderDict))

for xx in res:
    print(xx)
