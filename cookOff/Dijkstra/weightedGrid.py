'''
Created on 27-Mar-2017

@author: rjoshi
'''

class weightedGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = []
        
    def isPassable(self, idx):
        return idx not in self.walls
    
    def inBound(self, idx):
        (x, y) = idx
        return 0 <= x < self.width and 0 <= y < self.height
    
    def neighbours(self, idx):
        (x, y) = idx
        results = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        results = filter(self.isPassable, results)
        results = filter(self.inBound, results)
        return results
    
    def cost(self, f_node, t_node):
        (x, y) = t_node
        return self.weights[self.width*x + y]
    
    