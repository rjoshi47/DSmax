'''
Created on 09-Aug-2017

@author: rjoshi
'''
def match(pat, searchStr, piMtx):
    i = 0
    mLen = len(searchStr)
    pLen = len(pat)
    pCount = 0
    pIndex = 0
    while i < mLen:
        while i < mLen and pat[0] != searchStr[i]:
            i += 1
        if i >= mLen:
            break 
        else:
            count = 0
            tempI = i
            while count < pLen and i < mLen and pat[count] == searchStr[i]:
                count += 1
                i += 1
            if count > 0:
                if count > pCount:
                    pCount = count
                    pIndex = tempI
                #i = i + count
            elif i == mLen:
                break
            else:
                i = i - piMtx[count-1]
    return pIndex

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
            piMtx[i] = piMtx[i] + count
            i += 1
            k += 1
            count += 1
        k = 0
    #print(piMtx)
    return piMtx

n = input()
pt = input()
mStr = input()

#print(mStr)
#print(pt)
print(match(pt, mStr, processStr(mStr)))