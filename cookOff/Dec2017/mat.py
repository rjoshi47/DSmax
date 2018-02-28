'''
Created on 10-Dec-2017

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
    
que = priorityQueue()
que.put(2, 2)
que.put(5, 5)
que.put(3, 3)
que.put(1, 1)

print(que.get())
print(que.get())
print(que.get())
print(que.get())

