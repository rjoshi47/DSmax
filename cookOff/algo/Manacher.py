'''
Created on 07-May-2017

@author: rjoshi

Finding longest or all palindrome in a string in O(n) 

    Here we take advantage of the fact that palindromes are symmetric from center. 

    For string B C B A B C B 

        We start computing from left matching chars from center c and keeping track of r the right most boundary of the palindrome 

        After preprocessing and reaching A we get: 

            $ # B # C # B # A # B # C # B # @ 
            0 0 1 0 3 0 1 0 7 

                            C               R (boundary of palindrome) 

            Now we can simply copy values mirror characters from C to R with given condition 

            mirror = 2*C – i 

            If mirror < c: 

            p[i] = min( p[mirror], R - i) // P[i] holds palindrome lengths from given character   

            //Now we know p[i] is min length of palindrome from location i so we proceed matching after p[i] length 

            While p[i + p[i] + 1] == p[i- (p[i]+1)]: 

                P[i] += 1 

            If p[i] + i > R:  

                R = p[i] + i 

                C = i  

        Why min check is required 

            $ # A # B # C # B # A # B # C # B # @ 
            0 0 1 0 1 0 6 0 1 0 7 
                                C                      R 

            Now we cannot copy mirror value for C but we know within boundary it will be a palindrome we go fir R - i.  
'''

def getLongestPalinLength(arrStr):
    myGraph = {}
    temp = []
    temp.append('$')
    for i in range(0, len(arrStr)):
        temp.append('#')
        temp.append(arrStr[i])
    temp.append('#')
    temp.append('@')
    
    p = [0]*len(temp)
    
    c = 0
    r = 0
    print(temp)
    for i in range(1, len(temp)-1):
        mirror = 2*c - i
        
        if mirror < c:
            p[i] = min(r-i, p[mirror])
            
        while temp[i + p[i] + 1] == temp[i - (p[i] + 1)]:
            p[i] = p[i] + 1
        if i + p[i] > r:
            c = i 
            r = i + p[i]
    print(p[c])
#         if p[i] > 0:    
#             print(i,end=" ")
#             print((r, (i-p[i], i+p[i])))
#             if i-p[i] not in myGraph:
#                 l = []
#                 l.append(i+p[i])
#                 myGraph[i-p[i]] = l
#             else:
#                 l = myGraph[i-p[i]]
#                 l.append(i+p[i])
#                 myGraph[i-p[i]] = l
        
    
    #print(arrStr)
    print(p)
    print(myGraph)
    return p[c]
    
            
getLongestPalinLength('EABAEABAB')
getLongestPalinLength('AAAAAAA')
