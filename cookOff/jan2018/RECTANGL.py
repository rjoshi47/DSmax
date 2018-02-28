'''
Created on 06-Jan-2018

@author: rjoshi
'''
def bSearch(arr, num, l, r):
    if l > r:
        return -1
    else:
        m = int((l+r)/2)
        if m == l:
            if l+1 <= r and int(arr[m]) < num and int(arr[l+1]) >= num:
                return m
            elif m+1 == r and int(arr[r]) < num:
                return m+1
            else:
                return -1
        elif m == r:
            if int(arr[m]) < num:
                return m
            else:
                return -1
        elif int(arr[m]) < num:
            if m == r:
                return m
            elif m+1 <= r and int(arr[m+1]) >= num:
                return m
            else:
                return bSearch(arr, num, m, r)
        else:
            return bSearch(arr, num, l, m)

arr = [9,10,11,12,13,14]     
print(bSearch(arr,12, 0, len(arr)-1))