'''
https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting
Merge Sort: Counting Inversions
Minimum number of adjacent element swaps required to make array sorted.
We are using merge sort to break and merge array.
Example:
2134 
21 34
2 1    3 4
Merge [2] [1] cond2 applied here and swaps required are: (1+1 - 1) - 0 =>1 (which how far 1 is from actual position)
      
4213
42 13
4 2 1 3
Merge [4] [2] cond2 applied gives 1 inversion
Merge [1] [3] no inversion
Merge LA = [2 4]  RA = [1 3]
A = [2 4 1 3]
2 > 1: cond2 1 inversion
A = [1 4 1 3]
2 < 3:
A = [1 2 1 3] increment linv as the element from LA is choosen which means, 
      now if any element from RA is choosen next them it is off from its position by (sizeof LA - linv) = (sizeofLA - 1) = 2-1 =1
4 > 3:
A = [1 2 3 3] # cond2 applied gives (2-1) = 1 inversion
only 4 is remaining in LA
A = [1 2 3 4] Overall 2 inversion
'''
def merge(A, l, mid, r):
    leftA = list(A[l:mid+1])
    rightA = list(A[mid+1:r+1])
    print(leftA, end=" ")
    print(rightA)
    i = 0
    j = 0
    k = l
    inv1 = 0 # swaps to place a misplaced entry to its position
    linv = 0
    while i < len(leftA) and j < len(rightA):
        if leftA[i] <= rightA[j]: # cond1
            A[k] = leftA[i]
            i += 1
            linv += 1
        else: #cond2
            inv1 += (mid+1-l) - linv # Add the difference in actual position and position of that element in sorted array
            A[k] = rightA[j]
            j += 1
            #inv1 += 1
        k += 1
    
    while i < len(leftA):
        A[k] = leftA[i]
        i += 1
        k += 1
        
    while j < len(rightA):
        A[k] = rightA[j]
        j += 1
        k += 1
    
    return inv1
    
def splitMerge(A, l, r):
    if l < r:
        mid = int((l+(r-1))/2)
        splitMerge(A, l, mid)
        splitMerge(A, mid+1, r)
        global inv
        inv += merge(A, l, mid, r)

global inv
res = []
for _ in range(int(input())):
    n = input()
    A = list(map(int, input().split(" ")))
    B = list(A)
    
    inv = 0
    splitMerge(A, 0, len(A)-1)
    res.append(inv)

for xx in res:
    print(xx)

