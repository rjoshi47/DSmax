'''
Created on 18-May-2017

@author: rjoshi
'''
from myGraph.sQueue import sQueue
class myBFS(object):
    def __init__(self):
        self.graph = {}
        
    def neighbours(self, idx):
        if idx not in self.graph:
            return None
        return self.graph[idx]

def doBFS(graph, s, d):
    frontier = sQueue()
    frontier.put(0, s)
    came_from = {}
    cost_so_far = {}
    cost_so_far[s] = 0
    came_from[s] = None
    
    while not frontier.isEmpty():
        current = frontier.get()
        if current == d:
            break
        
        for nextNode in graph.neighbours(current):
            new_cost = cost_so_far[current] + 1
            if nextNode not in came_from or new_cost < cost_so_far[nextNode]:
                came_from[nextNode] = current
                cost_so_far[nextNode] = new_cost
                frontier.put(new_cost, nextNode)
    return came_from

def getPath(came_from, s, d):
    current = d
    path = [current]
    while current != s:
        current = came_from[current]
        path.append(current)
        #path.reverse()
    return path
graph = myBFS()
graph.graph[1] = [2]
graph.graph[2] = [3]
graph.graph[3] = [4,5]
graph.graph[4] = [5]

print(getPath(doBFS(graph, 1, 5), 1, 5))
