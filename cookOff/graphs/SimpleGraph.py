'''
Created on 25-Mar-2017

@author: rjoshi
'''

class SimpleGraph(object):
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, nodeId):
        return self.edges[nodeId]
    
    
    
    
        