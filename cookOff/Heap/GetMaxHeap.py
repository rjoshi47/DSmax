'''
Created on 13-Jul-2017

@author: rjoshi
'''
def compareSwap(heap, idx, hlen):
    lci = 2*idx + 1
    rci = 2*idx + 2
    lc = -1
    rc = -1
    #print(heap[idx])
    (p, mp) = heap[idx]
    if lci < hlen:
        (lc, ml) = heap[lci]
    if rci < hlen:
        (rc, mr) = heap[rci]
    if lc >= p and lc >= rc:
        heap[idx] = (lc, ml)
        heap[lci] = (p, mp)
        compareSwap(heap, lci, hlen)
    if rc > p and rc > lc:
        heap[idx] = (rc, mr)
        heap[rci] = (p, mp)
        compareSwap(heap, rci, hlen)
        
def maxHeapify(heap):
    n = len(heap)
    for i in range(int(n/2), -1, -1):
        compareSwap(heap, i, n)

def getMaxElement(heap, size):
    top = heap[0]
    heap[0] = heap[size-1]
    compareSwap(heap, 0, size - 1)
    size = size - 1
    return top

heap = [(6, (2,3,3)), (4, (2,3)), (1, (2,3)), (5, (2,3)), (6, (2,3)), (2, (2,3)), (3, (2,3)), (6, (2,3))]

(v, (a,b,c)) = heap[0]
print(a)

print(b)
print(c)

maxHeapify(heap)
size = len(heap)

vv = heap[0]


#while size > 0:
#    print(getMaxElement(heap, size))
#    size = size - 1