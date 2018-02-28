'''
Created on 03-Jun-2017

@author: rjoshi
'''

results = []
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

def process(l1, l2, l3):
    maxHeapify(l1)
    heapSort(l1)
    maxHeapify(l2)
    heapSort(l2)
    maxHeapify(l3)
    heapSort(l3)
    sum = 0
    #(a+b)*(b+c) = ab + ac + bb + bc = bb + b(a1+c1) + a1*c1 
    ii1 = 0
    ii3 = 0
    for i2 in range(0, len(l2)):
        num2 = l2[i2]
        for i1 in range(ii1, len(l1)):
            num1 = l1[i1]
            if num1 <= num2:
                #ii1 = i1+1
                for i3 in range(ii3, len(l3)):
                    num3 = l3[i3]
                    if num3 <= num2:
                        ii3 = i3+1
                        print()
                        print(num1,end=" ")
                        print(num2,end=" ")
                        print(num3,end=" ")
                        sum = sum + ((num1+num2)*(num3+num2))%1000000007
            else:
                break
    return sum
            
    
    
tests = int(input())
for i in range(0, tests):
    etc = input().split(" ")
    l1 = list(map(int, input().split(" ")))
    l2 = list(map(int, input().split(" ")))
    l3 = list(map(int, input().split(" ")))
    results.append(process(l1, l2, l3))
    
for xx in results:
    print(xx)
     
