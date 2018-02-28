'''
Created on 05-Sep-2017
LCS
@author: rjoshi
'''
s1 = "ABCBDAEB"
s2 = "BDCABAE"
w = len(s1) + 1
h = len(s2) + 1

LCS = [[0]*w for y in range(h)]

def computeLCS(s1, s2):
    s1 = '0'+s1
    s2 = '0'+s2
    for r in range(1, len(s2)):
        for c in range(1, len(s1)):
            print(r, c)
            if s1[c] == s2[r]:
                LCS[r][c] = 1 + LCS[r-1][c-1]
            else:
                LCS[r][c] = max(LCS[r][c-1], LCS[r-1][c])
        
def getSeq(s1, s2, ls1, ls2):
    if ls1 == 0 or ls2 == 0:
        return ""
    elif s1[ls1] == s2[ls2]:
        return getSeq(s1, s2, ls1-1, ls2-1) + (s2[ls2])
    else:
        if LCS[ls2][ls1-1] < LCS[ls2-1][ls1]:
            return getSeq(s1, s2, ls1, ls2-1)
        else:
            return getSeq(s1, s2, ls1-1, ls2)
    
def getSequence(s1, s2):
    computeLCS(s1, s2)
    for r in range(0, len(s2)+1):
        for c in range(0, len(s1)+1):
            print(LCS[r][c], end=" ")
        print()
    s1 = '0'+s1
    s2 = '0'+s2
    print(getSeq(s1, s2, len(s1)-1, len(s2)-1))
    
getSequence(s1, s2)