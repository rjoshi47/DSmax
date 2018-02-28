'''
Created on 09-Aug-2017
String matching
https://www.ics.uci.edu/~eppstein/161/960227.html
@author: rjoshi
'''
def match(pat, searchStr, piMtx):
    i = 0
    mLen = len(searchStr)
    pLen = len(pat)
    while i < mLen:
        while i < mLen and pat[0] != searchStr[i]:
            i += 1
        if i >= mLen:
            return -1 
        else:
            count = 0
            tempI = i
            while count < pLen and i < mLen and pat[count] == searchStr[i]:
                count += 1
                i += 1
            if count == pLen:
                #All matches start
                print(tempI)
                print(searchStr[tempI:tempI+pLen])
                i = tempI + pLen
                #All matches end
                
                #return tempI 
            elif i == mLen:
                return -1
            else:
                i = i - piMtx[count-1]

def processStr(mStr):
    mLen = len(mStr)
    piMtx = mLen*[0]
    k = 0
    i = 1
    while i < mLen:
        while k >= 0 and i < mLen and mStr[k] != mStr[i]:
            i += 1
        count = 1
        while i < mLen and mStr[k] == mStr[i]:
            piMtx[i] = count
            i += 1
            k += 1
            count += 1
        #k = 0
    print(piMtx)
    return piMtx

mStr = "bananananadnano"
pat = "nanadnano"

print(match(pat, mStr, processStr(pat)))