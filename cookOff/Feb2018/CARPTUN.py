'''
Created on 03-Feb-2018

@author: rjoshi
'''
res = []
for o in range(0, int(input())):
    tunnels = int(input())
    waitingTime = input().split(" ")
    cds = input().split(" ")
    
    c = int(cds[0])
    d = float(cds[1])
    s = float(cds[2])
    
    roadTime = d/s
    
    car1EscapeTiming = [0]*tunnels
    car1EscapeTiming[0] = float(waitingTime[0])
    for i in range(1, len(car1EscapeTiming)):
        car1EscapeTiming[i] = car1EscapeTiming[i-1] + float(waitingTime[i])
        
    car2EscapeTiming = [0]*tunnels
    car2EscapeTiming[0] = float(waitingTime[0])*2
    for i in range(1, len(car2EscapeTiming)):
        car2EscapeTiming[i] = (max(car2EscapeTiming[i-1] ,
                                   car1EscapeTiming[i])
                               + float(waitingTime[i]))
    
    #print(car1EscapeTiming)
    #print(car2EscapeTiming)
    #    print(car2EscapeTiming[tunnels-1])
    res.append((car2EscapeTiming[tunnels-1]
                - car1EscapeTiming[tunnels-1])*(c-1))
    
for xx in res:
    print(xx)