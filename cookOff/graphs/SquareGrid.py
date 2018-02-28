'''
Created on 26-Mar-2017

@author: rjoshi
'''

class SquareGrid:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.walls = []
        
    def inBound(self, idx):
        (x, y) = idx
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, idx):
        return idx not in self.walls
    
    def neighbours(self, idx):
        (x, y) = idx
        results = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        results = filter(self.inBound, results)
        results = filter(self.passable, results)
        return results
        
        