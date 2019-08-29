'''
Created on Aug 29, 2019
https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

create min heap of size = number of arrays 
now the min element will be at top.
- Remove element from top.
- Insert element from the array from which top element was removed. 
  - If top element was last element in its row then skip (it becomes merge k-1 sorted array problem).

@author: rjoshi
'''
import heapq
res = []
for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = list(map(int, input().strip().split(" ")))
    mat = [[0 for x in range(n)] for y in range(n)]
    
    i = 0
    for x in range(n):
        for y in range(n):
            mat[x][y] = nums[i]
            i += 1
    
    #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    minHeap = []
    for i in range(n):
        heapq.heappush(minHeap, (mat[i][0], (i, 0)))
         
    result = []
    while len(minHeap) != 0:
        pop = heapq.heappop(minHeap)
        result.append(pop[0])
        (pr, pc) = pop[1]
            
        if pc != n - 1:
            heapq.heappush(minHeap, (mat[pr][pc+1], (pr, pc+1)))
            

            
    print(result)
        
        
