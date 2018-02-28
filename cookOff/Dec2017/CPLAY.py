'''
Created on 03-Dec-2017

@author: rjoshi
'''
import sys
results = []
while True:
    ss = sys.stdin.readline()
    if ss == "" or ss == "\n":
        break
    g1 = 0
    g2 = 0
    ll = len(results)
    
    for k in range(0, len(ss)):
        if ss[k] != '\n':
            g = int(ss[k])
            if k % 2 == 0:
                g1 += g
            else:
                g2 += g
          
                    
            if k >= 5 and k <= 9:
                if (g1 - g2 >= 3) or (g1 - g2 == 2 and k >= 7) or (g1 - g2 == 1 and k ==9):
                    results.append("TEAM-A "+str(k+1))
                    break
                if (g2 - g1 >= 3) or (g2 - g1 == 2 and k >= 6) or (g2 - g1 == 1 and k>=8):
                    results.append("TEAM-B "+str(k+1))
                    break
            elif k >= 10 and k % 2 == 1:
                if g1 > g2:
                    results.append("TEAM-A "+str(k+1))
                    break
                elif g2 > g1:
                    results.append("TEAM-B "+str(k+1))
                    break
                
    if len(results) == ll:
        if g1 == g2:
            results.append("TIE")

for xx in results:
    print(xx)