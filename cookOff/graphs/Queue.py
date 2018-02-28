'''
Created on 25-Mar-2017

@author: rjoshi
'''
import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
        
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
        
    def get(self):
        return self.elements.popleft()