'''
Created on 05-Jul-2017

@author: rjoshi
'''
import heapq

class Node:
    def __init__(self):
        self.parent = None
        self.val = 0
        
class pQueue:
    def __init__(self):
        self.elements = []
                
    def isEmpty(self):
        return len(self.elements) == 0
    
    def put(self, p, item):
        heapq.heappush(self.elements, (p, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    

def MST(weigh, adjNodes, n, startNode):
    vertices = {}
    nodes = {}
    pq = pQueue()
    for key in range(1, n+1):
        node = Node()
        if key == startNode:
            node.val = 0
            pq.put(0, key)
        else:
            node.val = 10000000
            pq.put(10000000, key)
        nodes[key] = node
    
    
    while not pq.isEmpty():
        key = pq.get()
        currNode = nodes[key]
        if currNode.parent is not None:
            vertices[key] = currNode.parent
        for neBor in adjNodes[key]:
            if neBor not in vertices:
                vNode = nodes[neBor]
                if weigh[(neBor, key)] < vNode.key:
                    vNode.parent = key
                    vNode.key = weigh[(neBor, key)]
                    pq.put(currNode.key, currNode)
            
tests = int(input())    
for i in range(0, tests):
    weigh = {}
    adjNodes = {}
    (n, m) = input().split(" ")
    for j in range(0, int(m)):
        nums = input().split(" ")
        u = int(nums[0])
        v = int(nums[1])
        w = int(nums[2])
        weigh[(u,v)] = w
        weigh[(v,u)] = w
        
        if u not in adjNodes:
            nodeList = [v]
            adjNodes[u] = nodeList
        else:
            nodeList = adjNodes[u]
            nodeList.append(v)
            adjNodes[u] = nodeList
    MST(weigh, adjNodes, n, u)
