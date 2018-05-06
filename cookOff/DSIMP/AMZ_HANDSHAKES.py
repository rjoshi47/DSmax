'''
Created on 06-May-2018

@author: rjoshi
link: http://www.geometer.org/mathcircles/catalan.pdf
Using catalan numbers here to find number of non-crossing handshakes.

for n = 8 we have m = n/2 i.e 4 pairs.
Lets assume octagon is of form 
       1
   8       2
  7          3
   6       4
       5
Cm = number of non-crossing hand shakes with m number of pairs.
Now every time we draw a line between two pair of numbers on each side we have to leave even number of pairs (otherwise handshakes gonna cross).
Cosidering 1 we can draw lines in following manner.
1-2 this devides problem into 0 and 3 pairs.
1-4 this devides problem into 1 and 2 pairs.
1-6 into 2 and 1 pairs.
1-8 into 3 and 0 pairs.
So C4 = C0C3 + C1C2 + C2C1 + C3C0 = 1*5 + 1*2 + 2*1 + 5*1 = 14 (C3 and C2 can be precomputed in similar fashion)
'''

def getNonCrossingHandShakes(n):
    cat = [0]*(n+1)
    cat[0] = 1
    cat[1] = 1
    
    for i in range(2, n+1):
        for j in range(0,i):
            cat[i] += (cat[j]*cat[i-j-1])
            
    return cat[n]

res = []
for _ in range(0, int(input())):
    n = int(input().strip())
    res.append(getNonCrossingHandShakes(int(n/2)))
    
for xx in res:
    print(xx)
