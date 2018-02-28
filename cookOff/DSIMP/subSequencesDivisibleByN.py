'''
Created on 08-Jan-2018
int countDivisibleSubseq(string str, int n)
{
    int len = str.length();
 
    int dp[len][n];
    memset(dp, 0, sizeof(dp));
 
    dp[0][(str[0]-'0')%n]++;
 
    for (int i=1; i<len; i++)
    {
        dp[i][(str[i]-'0')%n]++;
        for (int j=0; j<n; j++)
        {
            dp[i][j] += dp[i-1][j];
            dp[i][(j*10 + (str[i]-'0'))%n] += dp[i-1][j];
        }
    }
 
    return dp[len-1][0];
}
@author: rjoshi
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
    
#     print(" ")
#     dp = [[0]*n for y in range(nLen)]
# 
#     dp[0][0] += 1
#     dp[0][int(numStr[0]) % n] += 1
#     
#     for i in range(1, nLen):
#         for j in range(0, n):
#             dp[i][j] += dp[i - 1][j]
#         for j in range(0, n):
#             dp[i][(j*10 + int(numStr[i])) % n] += dp[i-1][j]
#             
#     for i in range(0, nLen):
#         for j in range(0, n):
#             print(dp[i][j], end=" ")
#         print(" ")
        
countSeqDiv("1234", 4)