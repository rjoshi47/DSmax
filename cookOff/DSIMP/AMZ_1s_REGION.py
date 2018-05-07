'''
Created on 07-May-2018

@author: rjoshi
Just a simple BFS/DFS over the matrix.

Iterate nxm matrix if m[i][j] == 1 and not visted yet perform BFS and count all reachable nodes 
from (i,j) which forms one cluster with value euqals count of all reachable nodes. 

x-1,y-1     x-1,y   x-1,y+1
x,y-1    x,y     x,y+1
x+1,y-1     x+1,y   x+1,y+1
1
4 5
0 0 1 1 0 1 0 1 1 0 0 1 0 0 0 0 0 0 0 1
'''
import heapq
class Matrix:
    def __init__(self, width, height, mFill):
        self.width = width
        self.height = height
        self.validCell= mFill

    def in_bound(self, position):
        (x, y) = position
        return (0 <= x < self.height 
                    and 0 <= y < self.width 
                        and (x,y) in self.validCell)

    def neighbors(self, idx):
        (x, y) = idx
        nbors = [(x-1, y-1), (x-1, y), 
                 (x-1, y+1), (x, y-1),
                 (x,y+1), (x+1, y-1),
                 (x+1, y), (x+1, y+1)]
        
        return filter(self.in_bound, nbors)
    
class PriorityQueue:
    def __init__(self):
        self.elements = []
        
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item):
        heapq.heappush(self.elements, item)
    
    def get(self):
        return heapq.heappop(self.elements)

def onesGroup(graph, start, visited):
    frontier = PriorityQueue()
    frontier.put(start)
    count1s = 1
    visited[start] = 1
    
    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in visited:
                count1s += 1
                visited[next] = 1
                frontier.put(next)    
    return count1s
  
res = []
for _ in range(0, int(input())):
    (h, w) = input().split(" ")
    w = int(w)
    h = int(h)
    tnums = input().split(" ")
    nums = []
    for k in range(0, len(tnums)):
        if len(tnums[k]) > 0:
            nums.append(int(tnums[k]))
    
    k = 0
    mFill = {}
    for i in range(0, h):
        for j in range(0, w):
            if nums[k] == 1:
                mFill[(i,j)] = 1
            k += 1
    k = 0
    count = 0
    visited = {}
    graph = Matrix(int(w), int(h), mFill)
    for i in range(0, h):
        for j in range(0, w):
            if nums[k] == 1 and nums[k] not in visited:
                count = max(count, onesGroup(graph, (i,j), visited))
            k += 1
        
    res.append(count)

for xx in res:
    print(xx)
