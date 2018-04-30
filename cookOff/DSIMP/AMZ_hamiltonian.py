'''
Created on Apr 30, 2018

@author: rjoshi
'''
res = [1,2,3]
pri
def isHamiltonian(graph, start, vertexCount):
    mqueue = [1,2,3]
    mqueue.pop()
    
for _ in range(0, int(input())):
    (v, e) = input().split(" ")
    tEdges = input().split(" ")
    edges = []
    for k in range(0, len(tEdges)):
        if len(tEdges[k]) > 0:
            edges.append(tEdges[k])
    
    graph = {}
    for k in range(0, len(edges)-1):
        if k+1 < len(edges):
            if edges[k] not in graph:
                graph[edges[k]] = [edges[k+1]]
            else:
                graph[edges[k]].append(edges[k+1])
    
