'''
Created on 22-Dec-2017

@author: rjoshi
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def arrayRotate(arr, d):
    n = len(arr)
    for i in range(0, gcd(d, n)):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    print(arr)
    
arrayRotate([1,2,3,4,5,6,7], 3)
    