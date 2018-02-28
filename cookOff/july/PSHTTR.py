'''
Created on 09-Jul-2017

@author: rjoshi
'''
import heapq
class Queue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, item):
        heapq.heappush(self.elements, item)
        
    def get(self):
        return heapq.heappop(self.elements)

def getCost(came_from, start, goal, k, costs):
    current = goal
    fa = 0
    u = current
    c1 = 0
    while current != start:
        v = came_from[current]
        c1 = costs[(u, v)]
        if c1 <= k:
            fa = fa^c1
        current = came_from[current]
        u = current
    return fa


def dijkstraSearch(graphDict, fromNode, toNode):
    frontier = Queue()
    frontier.put(fromNode)
    came_from = {}
    came_from[fromNode] = None
    while not frontier.isEmpty():
        current = frontier.get()
        if current == toNode:
            break
        
        for nextNode in graphDict[current]:
            if nextNode not in came_from:
                frontier.put(nextNode)
                
                came_from[nextNode] = current
    return came_from

res = []
tests = int(input())
for i in range(0, tests):
    graphDict = {}
    costs = {}
    vts = int(input())
    for j in range(0, vts-1):
        nums = input().split(" ")
        u = int(nums[0])
        v = int(nums[1])
        w = int(nums[2])
        if u in graphDict:
            ls = graphDict[u]
            ls.append(v)
            graphDict[u] = ls
        else:
            ls = []
            ls.append(v)
            graphDict[u] = ls
        if v in graphDict:
            ls = graphDict[v]
            ls.append(u)
            graphDict[v] = ls
        else:
            ls = []
            ls.append(u)
            graphDict[v] = ls
        
        costs[(u,v)] = w
        costs[(v,u)] = w
    q = int(input())
    pathDict = {}
    for k in range(0, q):
        nums = input().split(" ")
        u = int(nums[0])
        v = int(nums[1])
        k = int(nums[2])
        if (u,v) in pathDict:
            path = pathDict[(u,v)]
            cost = getCost(path, u, v, k, costs)
        elif (v, u) in pathDict:
            path = pathDict[(v,u)]
            cost = getCost(path, v, u, k, costs)
        else:
            path = dijkstraSearch(graphDict, u, v)
            pathDict[(u,v)] = path
            cost = getCost(path, u, v, k, costs)
        res.append(cost)
    

for ss in res:
    print(ss)