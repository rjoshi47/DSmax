'''
Created on 26-Mar-2017

@author: rjoshi
'''
from graphs.Queue import Queue
from graphs.SquareGrid import SquareGrid
def BFS(graph, start):
    frontier = Queue()
    frontier.put(start)
    cameFrom = {}
    cameFrom[start] = None
    
    while not frontier.isEmpty():
        current = frontier.get()
        for nextCell in graph.neighbours(current):
            if nextCell not in cameFrom:
                cameFrom[nextCell] = current
                frontier.put(nextCell)
    return cameFrom

def getPath(start, goal, cameFrom):
    current = goal
    path = [current]
    while current != start:
        current = cameFrom[current]
        path.append(current)
    #path.append(start)
    path.reverse()
    print(path)

graph = SquareGrid(5,5)
graph.walls = [(0,1), (1,1), (3,0), (3,2) , (3,3), (1,3), (2,3)]

cameFrom = BFS(graph, (0,0))

getPath((0,0), (4,4), cameFrom)



