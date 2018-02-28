'''
Created on 18-May-2017

@author: rjoshi
'''

import heapq
class sQueue:
    def __init__(self):
        self.elements = []
        
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, p, item):
        heapq.heappush(self.elements, (p, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]