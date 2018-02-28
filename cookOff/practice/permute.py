'''
Created on 29-Apr-2017

@author: rjoshi
'''

from practice.Grid import Grid
from practice.QUeue import Queue

myDict = {}

def BFSPermute(start, graph):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = None
    
    tList = []

    while not frontier.isEmpty():
        current = frontier.get()
        if visited[current] != None:
            tList.append((visited[current], current))
        for nextNode in graph.neighbours(current):
            if nextNode not in visited:
                frontier.put(nextNode)
                visited[nextNode] = current
    return tList

graph = Grid(4)

myDict[(1,1)] = BFSPermute(1, graph)
myDict[(2,1)] = BFSPermute(2, graph)
myDict[(3,1)] = BFSPermute(3, graph)
myDict[(4,1)] = BFSPermute(4, graph)

print(myDict[(1,1)] )
print(myDict[(2,1)] )
print(myDict[(3,1)] )
print(myDict[(4,1)] )

nodes12 = myDict[(1,1)] 

