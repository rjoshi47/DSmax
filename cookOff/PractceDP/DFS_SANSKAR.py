'''
Created on 27-Jan-2018

@author: rjoshi
'''
import heapq
class sQueue:
    def __init__(self):
        self.elements = []
        
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, p, item):
        heapq.heappush(self.elements, (p, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
class SimpleGraph():
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, nodeId):
        return self.edges[nodeId]
    
def doBFS(graph, s, d):
    frontier = sQueue()
    frontier.put(0, s)
    came_from = {}
    cost_so_far = {}
    cost_so_far[s] = s
    came_from[s] = None
    
    while not frontier.isEmpty():
        current = frontier.get()
        if cost_so_far[current] == d:
            print(current)
            print(came_from)
            print(cost_so_far)
            print()
            break
        
        for nextNode in graph.neighbors(current):
            new_cost = cost_so_far[current] + nextNode
            if nextNode not in came_from and new_cost <= d:
                came_from[nextNode] = current
                cost_so_far[nextNode] = new_cost
                frontier.put(new_cost, nextNode)
    return came_from
                
test_graph = SimpleGraph()
test_graph.edges = {
    1 : [2,4,5,6],
    2 : [1,4,5,6],
    4 : [1,2,5,6],
    5 : [1,2,4,6],
    6 : [1,2,4,5]
    }
                
doBFS(test_graph, 1, 5)
                
                