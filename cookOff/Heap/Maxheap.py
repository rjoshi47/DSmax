'''
Created on 20-Apr-2017

@author: rjoshi
'''

def compareSwap(heap, idx, hlen):
    lci = 2*idx + 1
    rci = 2*idx + 2
    lc = -1
    rc = -1
    p = heap[idx]
    if lci < hlen:
        lc = heap[lci]
    if rci < hlen:
        rc = heap[rci]
    if lc >= p and lc >= rc:
        heap[idx] = lc
        heap[lci] = p
        compareSwap(heap, lci, hlen)
    if rc > p and rc > lc:
        heap[idx] = rc
        heap[rci] = p
        compareSwap(heap, rci, hlen)
        
def maxHeapify(heap):
    n = len(heap)
    for i in range(int(n/2), -1, -1):
        compareSwap(heap, i, n)


def heapSort(heap):
    f = 0
    l = len(heap) - 1
    for i in range(l, 0, -1):
        temp = heap[0]
        heap[0] = heap[l-f]
        heap[l-f] = temp
        compareSwap(heap, 0, l-f)
        f = f + 1
        
heap = [3,4,2,10,7,8,6,9,12,14,11,1,5,12,40,11,29,11,2,3,4,5,6,17,90]
#heap = [3,1]
maxHeapify(heap)
print(heap)
heapSort(heap)
print(heap)

lst = [(221,3), (12,2), (2,5), (23,1), (25,6), (22,1)]
lst.sort(key=lambda x:x[0])
print(lst)