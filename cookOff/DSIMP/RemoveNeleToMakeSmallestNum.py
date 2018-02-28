'''
Created on 26-Dec-2017

@author: rjoshi
'''

def buildLowestNumberRec(mstr, n, res):
    if n == 0:
        res += mstr
        print(res)
        return
    
    if len(mstr) <= n:
        print(res)
        return
    
    mi = 0
    for i in range(1, n+1):
        if int(mstr[i]) <= int(mstr[mi]):
            mi = i
    res += mstr[mi]
    newstr = mstr[mi+1:len(mstr)]
    #print(res)
    buildLowestNumberRec(newstr, n-mi, res)
    
def util(str1, n):
    res = ""
    buildLowestNumberRec(str1, n, res)
    print(res)
    
str1 = "567891234"
n = 7
util(str1, n)
