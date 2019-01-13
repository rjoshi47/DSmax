'''
Created on 08-Jan-2018

@author: rjoshi
If we have a sequence p[1], p[2], ..., p[k] and know r, the remainder of the number p[1] p[2] ... p[k] modulo D, 
and then add p[k+1] to the sequence,
the remainder s of the new number p[1] p[2] ... p[k] p[k+1] modulo D is easy to compute: s = (r * 10 + p[k+1]) mod D.
'''

def countSeqDiv(numStr, n):
    nLen = len(numStr)
    dp = [[0]*n for y in range(nLen)]
    dp[0][int(numStr[0])] += 1
    
    for i in range(1, nLen):
        dp[i][int(numStr[i]) % n] += 1
        
        for j in range(0, n):
            dp[i][j] += dp[i-1][j]
            dp[i][(j*10 + int(numStr[i])) % n] += dp[i-1][j]
    
    for i in range(0, nLen):
        for j in range(0, n):
            print(dp[i][j], end=" ")
        print(" ")
        
countSeqDiv("1234", 4)
