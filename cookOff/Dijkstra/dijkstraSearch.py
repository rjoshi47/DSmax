'''
Created on 27-Mar-2017

@author: rjoshi
'''
from Dijkstra.priorityQueue import priorityQueue
from Dijkstra.weightedGrid import weightedGrid
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
                frontier.put(new_cost, nextNode)
                came_from[nextNode] = current
    return came_from

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    #path.append(start) # optional
    path.reverse() # optional
    return path            
graph = weightedGrid(5,5)
graph.weights = [1,1,1,2,1, 6,8,1,4,2, 1,1,1,12,3, 1,7,8,3,4, 1,1,1,1,1]
    
came_from = dijkstraSearch(graph, (0,0), (4,4))
print(reconstruct_path(came_from, (0,0), (4,4)))