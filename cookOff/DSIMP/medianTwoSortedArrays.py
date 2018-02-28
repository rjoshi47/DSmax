'''
Created on 24-Oct-2017
http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
@author: rjoshi
'''
arr = [1,2,3,4,5]
print(arr[1:3])
def getMedian(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    if n == 0 and m == 0:
        return -1
    elif n == 1 and m == 1:
        return (arr1[0] + arr2[0])/2
    elif n == 1:
        med = int(m/2)
        if m % 2 == 0:
            if arr1[0] > arr2[med]:
                return arr1[0]
            elif arr1[0] < arr2[med-1]:
                arr2[med-1]
            else:
                return med
        else:
            if arr1[0] < arr2[med]:
                if arr1[0] > arr2[med-1]:
                    return (arr1[0] + arr2[med])/2
                else:
                    return (arr2[med-1] + arr2[med])/2
            else:
                if arr1[0] > arr2[med]:
                    if arr1[0] > arr2[med+1]:
                        return (arr2[med] + arr2[med+1])/2
                    else:
                        return (arr1[0] + arr2[med])/2
    elif (n == 2 and m == 3) or (n == 3 and m == 2):
        temp = []
        for a in arr1:
            temp.append(a)
        for a in arr2:
            temp.append(a)
        temp.sort()
        return temp[int(len(temp)/2)]
    else:
        medArr1 = arr1[int(n/2)]
        medArr2 = arr1[int(n/2)]
        if medArr1 > medArr2:
            if n >= 4 and n % 2 == 0:
                arr1 = arr1[int(n/2):n]
            if n >= 5 and n%2 == 1:
                arr1 = arr1[int(n/2)+1:n]
            if m >= 4 and m % 2 == 0:
                arr1 = arr1[int(n/2):n]
            if n >= 5 and n%2 == 1:
                arr1 = arr1[0:int(n/2)]
            
            
            
            
            
            
            