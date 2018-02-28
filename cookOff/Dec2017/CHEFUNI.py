'''
Created on 09-Dec-2017

@author: rjoshi
'''
import heapq
from math import sqrt
class priorityQueue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, priority, item):
        heapq.heappush(self.elements, (priority, item))
        
    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(fromNode, toNode):
    (x1, y1, z1) = fromNode
    (x2, y2, z2) = toNode
    return sqrt(abs(x1-x2)^2 + abs(y1 - y2)^2 + abs(z1-z2)^2)

class myGraph:
    def __init__(self, a, b, c):
        self.costs = []
        self.costs.append(a)
        self.costs.append(b)
        self.costs.append(c)
        
        
    def neighbours(self, idx):
        (x, y, z) = idx
        results = [(x+1, y, z), (x, y+1, z), (x, y, z+1), (x+1, y+1, z), (x, y+1, z+1), (x+1, y, z+1), (x+1,y+1,z+1)]
        return results
    
    def cost(self, f_node, t_node):
        (x2, y2, z2) = t_node
        
        if f_node == (x2-1, y2, z2) or f_node == (x2, y2-1, z2) or f_node == (x2, y2, z2-1):
            return self.costs[0]
        elif f_node == (x2-1, y2-1, z2) or f_node == (x2, y2-1, z2-1) or f_node == (x2-1, y2, z2-1):
            return self.costs[1]
        else:
            return self.costs[2]
        
def dijkstraSearch(graph, fromNode, toNode):
    frontier = priorityQueue()
    frontier.put(0, fromNode)
    came_from = {}
    cost_so_far = {}
    came_from[fromNode] = None
    cost_so_far[fromNode] = 0
    
    while not frontier.isEmpty():
        current = frontier.get()
        #print(current)
        if current == toNode:
            break
        
        for nextNode in graph.neighbours(current):
            new_cost = graph.cost(current, nextNode) + cost_so_far[current]
            if nextNode not in came_from or new_cost < cost_so_far[nextNode]:
                cost_so_far[nextNode] = new_cost
                priority = new_cost + heuristic(toNode, nextNode)
                frontier.put(priority, nextNode)
                came_from[nextNode] = current
    return cost_so_far[toNode]

res = []
tests = int(input())
for i in range(0, tests):
    nums = input().split(" ")
    graph = myGraph(int(nums[3]), int(nums[4]), int(nums[5]))
    res.append(dijkstraSearch(graph, (0, 0, 0), (int(nums[0]), int(nums[1]), int(nums[2]))))
    
for xx in res:
    print(xx)