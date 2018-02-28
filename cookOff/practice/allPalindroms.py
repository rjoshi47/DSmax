'''
Created on 30-Apr-2017

@author: rjoshi
'''
def checkPalindrom(arr, i, loc, mid):
    l = i - 1
    r = i + 1
    while l >= 0 and r < len(arr) and arr[l] == arr[r] :
        loc[i] = str(int(loc[i]) + 1)
        l = l - 1
        r = r + 1
    
    l = i
    r = i + 1
    while l >= 0 and r < len(arr) and arr[l] == arr[r] :
        mid[i] = str(int(mid[i]) + 1)
        l = l - 1
        r = r + 1
    
    
def allPalindroms(arr):
    loc = len(arr)*['0']
    mid = len(arr)*['0']
    for i  in range (0, len(arr)):
        checkPalindrom(arr, i, loc, mid)
    print(arr)
    print(loc)
    print(mid)
    
allPalindroms(list("ababbbbabbababa"))
allPalindroms(list("aaabba"))
        
