'''
Created on 18-Dec-2017
@author: rjoshi

We store elements in stack and pop elements till the top element of stack 
is not smaller than current element.

- if stack becomes empty that indicates there is no element smaller on left for current number.
- otherwise the top element is smaller than current element so just print top stack element 
    and add current element to the stack.

'''


def nearestSmallestNumberOnLeft(arr):
    stak = []
    retValue = ''
    for i in range(0, len(arr)):
        while len(stak) != 0 and stak[len(stak)-1] >= arr[i]:
            stak.pop()
        
        if len(stak) == 0:
            retValue += '_ '
        else:
            retValue += str(stak[len(stak)-1]) +' '
        
        stak.append(arr[i])
    return retValue

arr = [4,5,1,8,15,17,6,4]
print(nearestSmallestNumberOnLeft(arr))