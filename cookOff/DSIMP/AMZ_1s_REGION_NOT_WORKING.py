'''
x-1,y-1	 x-1,y   x-1,y+1
x,y-1    x,y     x,y+1
x+1,y-1	 x+1,y   x+1,y+1

INPROGRESS ()

'''
class Matrix:
    def __init__(self, width, height):
        self.width = width
	self.height = height

    def in_bound(self, position):
        (x, y) = position
	return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, id):
        (x, y) = id
        nbors = [(x-1, y-1), (x-1, y), 
                 (x-1, y+1), (x, y-1),
                 (x,y+1), (x+1, y-1),
                 (x+1, y), (x+1, y+1)]
        
        return filter(self.in_bound, nbors)

def onesGroup(graph, start, visited, mFill):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    count1s = 1
    visited[start] = 1
    
    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
	    if next not in visited and next in mFill:
		count1s += 1
		visited[next] = 1
		frontier.put(next)    
    return count1s
  
res = []
for _ in range(0, int(input())):
    (w, h) = input().split(" ")
    graph = Matrix(int(w), int(h))
    tnums = input().split(" ")
    nums = []
    for k in range(0, len(tnums)):
        if len(tnums[k]) > 0:
	    nums.append(int(tnums[k]))
    
    k = 0
    matrix = [[0 for i in range(0, w)] for j in range(0, h)]
    for i in range(0, h):
	for j in range(0, w):
	    if nums[k] == 1:
	        mFill[(i,j)] = 1
	    k += 1
	    
    count = 0
    visited = {}
    for i in range(0, h):
	for j in range(0, w):
	    if nums[k] == 1 and nums[k] not in visited:
	        count = max(count, onesGroup(graph, (i,j), visited, mFill))
	    k += 1
	    
    res.append(count)
    
