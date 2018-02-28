'''
Created on 20-Aug-2017

@author: rjoshi
Going from left to right, keep track of the number of sequences until the current position, 
which are of these three forms:
1) a^i
2) a^i b^j
3) a^i b^j c^k
Suppose that these are stored in three variables a,b,c respectively. 
Whenever you see the character 'a', it can extend the strings of type 1, and also, 
be the starting position for a string of type 1, so a+=(a+1), 
whenever you see a 'b', it can extend previous strings of type 1 and 2, so b+=(a+b), for 'c', 
it will extend all strings of type 2 and 3, so c+=(b+c).
'''
sStr = "abcabc"

a = b = c = 0
for i in range(0, len(sStr)):
    if sStr[i] == 'a':
        a = a + (a + 1)
    elif sStr[i] == 'b':
        b = b + (a + b)
    elif sStr[i] == 'c':
        c = c + (c + b)
print(c)
