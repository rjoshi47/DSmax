'''
Created on 29-Apr-2017

@author: rjoshi
'''

class Grid(object):
    
    def __init__(self, side):
        self.side = side
        self.adjacentNodes = []
        for i in range(1, side+1):
            self.adjacentNodes.append(i)
        
    def inBound(self, idx):
        return 1 <= idx <= self.side
    
    def neighbours(self, idx):
        results = list(self.adjacentNodes)
        results.remove(idx)
        results = filter(self.inBound, results)
        return results
        