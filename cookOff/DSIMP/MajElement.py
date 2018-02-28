'''
Created on 22-Oct-2017
http://www.geeksforgeeks.org/majority-element/
@author: rjoshi
'''

def getMajEle(arr):
    count = 1
    majIdx = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[majIdx]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            majIdx = i
            count = 1
    print(arr[majIdx])
    
arr = [9,1,2,1,3,1,2]
getMajEle(arr)