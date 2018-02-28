'''
Created on 27-Dec-2017

@author: rjoshi
'''

def findOccOfN(numArr, l, r, num):
    return (findOcc(numArr, l, r, num, 'l'), findOcc(numArr, l, r, num, 'r'))

def findOcc(numArr, l, r, num, dir):
    if l > r:
        return -1
    
    m = int((l+r)/2)
    if numArr[m] == num:
        if dir == 'l':
            if m == 0 or (m - 1 >= l and numArr[m-1] != num):
                return m
            else:
                return findOcc(numArr, l, m, num, dir)
        else:
            if (m+1 == r and numArr[m+1] == num):
                return m + 1
            elif (m + 1 <= r and numArr[m+1] != num):
                return m
            else:
                return findOcc(numArr, m, r, num, dir)  
    elif numArr[m] > num:
        return findOcc(numArr, l, m, num, dir)
    else:
        return findOcc(numArr, m, r, num, dir)
    
numArr = [1,1,2, 2,2,2,2,3,3,4]
print(findOccOfN(numArr, 0, len(numArr)-1, 2))