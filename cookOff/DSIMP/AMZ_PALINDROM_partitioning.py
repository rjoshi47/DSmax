'''
Created on 19-May-2018

@author: rjoshi

1
bqbkb
['$', '#', 'b', '#', 'q', '#', 'b', '#', 'k', '#', 'b', '#', '$']
[0, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 0]
{1: [3, 7], 3: [1], 5: [7, 11], 7: [1, 5], 9: [11], 11: [5, 9]}
{11: 5, 1: None, 3: 1, 5: 7, 7: 1}
2


'''
res = []
import heapq

class pqueue:
    def __init__(self):
        self.elements = []
        
    def put(self, p, idx):
        heapq.heappush(self.elements, (p,idx))
        
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def isEmpty(self):
        return len(self.elements) == 0

def dijSearch(start, goal, intervalDict):
    frontier = pqueue()
    frontier.put(0, start)
    cost_so_far = {}
    came_from = {}
    cost_so_far[start] = 0
    came_from[start] = None
    
    while not frontier.isEmpty():
        current = frontier.get()
        if current == goal:
            break
        if current in intervalDict:
            for nextNode in intervalDict[current]:
                newCost = cost_so_far[current] + 1
                if nextNode not in cost_so_far or newCost < cost_so_far[nextNode]:
                    cost_so_far[nextNode] = newCost
                    came_from[nextNode] = current
                    frontier.put(newCost, nextNode)
    return came_from

def getPalPartitions(mstr):
    tempStr = ['$']
    for k in range(0, len(mstr)):
        tempStr.append('#')
        tempStr.append(mstr[k])
    tempStr.append('#')
    tempStr.append('$')
        
    p = [0]*len(tempStr)
    c = 1
    r = 2
    
    for i in range(1, len(tempStr)-1):
        m = 2*c - i
        
        if m < c and m >= 0 and r-i >=0:
            p[i] = min(p[m], r-i)
        
        while i + p[i] + 1 < len(tempStr)-1 and tempStr[i + p[i] + 1] == tempStr[i - (p[i] + 1)]:
            p[i] += 1
            
        if p[i] + i > r:
            r = p[i] + i
            c = i 
    print(tempStr)
    print(p)
    # build intervals
    intervalDict = {}
    intArr = [1]*len(mstr)
    for k in range(0, len(p)):
        if p[k] != 0:
            s = k - p[k]
            e = k + p[k]
            if s not in intervalDict:
                intervalDict[s] = [e]
            else:
                ed = intervalDict[s]
                ed.append(e)
                intervalDict[s] = ed
            if e not in intervalDict:
                intervalDict[e] = [s]
            else:
                ed = intervalDict[e]
                ed.append(s)
                intervalDict[e] = ed
    print(intervalDict)
    came_from = dijSearch(1, len(p)-2, intervalDict)
    #print(len(p)-2)
    count = 0
    start = len(p) - 2
    print(came_from)
    while came_from != None and start in came_from and came_from[start] != None:
        count += 1
        start = came_from[start]
    #print(count)
    return count - 1

   
for _ in range(0, int(input())):
    mstr = input().strip()
    res.append(getPalPartitions(mstr))
    
    
for xx in res:
    print(xx)
   
