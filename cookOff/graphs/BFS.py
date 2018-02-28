'''
Created on 25-Mar-2017

@author: rjoshi
'''
from graphs.Queue import Queue
from graphs.SimpleGraph import SimpleGraph
def BFS(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.isEmpty():
        current = frontier.get();
        print(current)
        for nextNode in graph.neighbors(current):
            if nextNode not in visited:
                visited[nextNode] = True
                frontier.put(nextNode)

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

BFS(example_graph, 'A')

         
                
                