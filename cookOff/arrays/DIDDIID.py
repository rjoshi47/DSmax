'''
Created on 14-Oct-2017

@author: rjoshi

https://practice.geeksforgeeks.org/problems/number-following-a-pattern/0
Input
5
D
I
DD
IIDDD
DDIDDIID

'''

res = []
for _ in range(0, int(input())):
    mSeq = input().rstrip() #sequence DDIDDIID
    liIndex = -1
    maxSofar = 0
    
    fNum = [0]*(len(mSeq)+1) # final result with one extra element
    fi = 0
    k = 0
    isStartingI = True # is sequence starting with I
    
    while k < len(mSeq):
        symbol = mSeq[k]
        if symbol == 'D':
            isStartingI = False
            dCount = 1
            while k + 1 < len(mSeq) and mSeq[k+1] == 'D': 
                dCount += 1
                k += 1
            #Count all D chars
            if liIndex == -1:
                '''
                Indicates start of the sequence so just fill array with decreasing values of dCount.
                '''
                fNum[fi] = dCount + 1
                maxSofar = dCount + 1
                fi += 1
                while dCount > 0:
                    fNum[fi] = dCount
                    fi += 1
                    dCount -= 1
            else:
                '''
                if an I is previously found in the sequence then we increase its value with dCount.
                Then we fill rest values by just subtracting -1 from previous value.
                '''
                fNum[liIndex] += dCount 
                maxSofar = fNum[liIndex]
                
                fi = liIndex + 1
                while dCount > 0:
                    fNum[fi] = fNum[fi-1] - 1
                    fi += 1
                    dCount -= 1
        else:
            # If I is found we just fill it with 1 + maxSoFar value found
            liIndex = fi
            maxSofar += 1
            fNum[fi] = maxSofar 
            fi += 1
            # One extra value need to be filled if sequence starting with I
            if isStartingI:
                liIndex = fi
                maxSofar += 1
                fNum[fi] = maxSofar 
                fi += 1
                isStartingI = False
        k += 1
    
    # Append array values as string
    res.append(''.join(str(x) for x in fNum)) 
                
for xx in res:
    print(xx)
