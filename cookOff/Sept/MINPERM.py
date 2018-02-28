'''
Created on 01-Sep-2017

@author: rjoshi
'''
tests = int(input())
res = []
for i in range(0, tests):
    n = int(input())
    rStr = ""
    eo = 1
    if n % 2 == 0:
        eo = 0
    if eo == 0:
        for k in range(1, n+1, 2):
            if rStr == "":
                rStr = str(k+1) + " "  + str(k)
            else:
                rStr = rStr + " " +  str(k+1) + " "  + str(k)
            
    if eo == 1:
        for k in range(1, n-1, 2):
            if k == n -2:
                if rStr == "":
                    rStr = str(k+1) + " " + str(k+2) + " " + str(k)
                else:
                    rStr = rStr + " " + str(k+1) + " " + str(k+2) + " " + str(k)
            elif rStr == "":
                rStr = str(k+1) + " "  + str(k)
            else:
                rStr = rStr + " " +  str(k+1) + " "  + str(k)

    res.append(rStr)

for xx in res:
    print(xx)