'''
Created on 14-Oct-2017

Alternate sorted path with path ending at element from array B

For Example 
A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
@author: rjoshi
'''
import collections
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.appendleft(x)
        
    def get(self):
        return self.elements.popleft()
        
class myGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, idx):
        if idx not in self.edges:
            return []
        return self.edges[idx]

def getPath(came_from, node):
    path = []
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.reverse()
    print(path)
    
def DFS(graph, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.isEmpty():
        current = frontier.get();
        nebors = graph.neighbors(current)
        for nextNode in nebors:
                came_from[nextNode[0]] = current
                if nextNode[1] == 2:
                    getPath(came_from, nextNode[0])
                frontier.put(nextNode[0])
               
                
example_graph = myGraph()
example_graph.edges = {
    10 : [(30, 2), (20, 2)],
    20 : [(25, 1)],
    25 : [(30, 2)],
    15 : [(30, 2) , (20, 2)],
}

DFS(example_graph, 10)
DFS(example_graph, 15)
DFS(example_graph, 25)
    



















