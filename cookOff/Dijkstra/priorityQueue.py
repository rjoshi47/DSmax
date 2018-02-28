'''
Created on 27-Mar-2017

@author: rjoshi
'''
import heapq
class priorityQueue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, priority, item):
        heapq.heappush(self.elements, (priority, item))
        
    def get(self):
        return heapq.heappop(self.elements)[1]
