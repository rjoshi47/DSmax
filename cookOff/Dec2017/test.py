tests = int(input())  
 
results = []  
 
def getSum(msum): 
    sE = 0 
    sO = 0 
    my_list = [int(d) for d in str(msum)]  
    for k in range(0, len(my_list)):  
        if my_list[k] % 2 == 0:  
            sE += my_list[k]  
        else:  
            sO += my_list[k] 
    return (sE, sO) 
 
#print(getSum(12344)) 
 
for z in range(0, tests):  
    n = int(input())   
    arr = []  
    gsum = 0 
    sE = 0  
    sO = 0  
    ded = 0 
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i+j, end=" ")
            
    ssum = 0
    for i in range(1, n+1):
        tsum = 0
        for j in range(1, n+1):
            (se, so) = getSum(i+j)
            tsum += abs(se- so)
            print(i+j, end = " ")
       
    for i in range(1, n+1):
        (sE, sO) = getSum(i + 1)
        gsum += abs(sE - sO)
        arr.append(abs(sE - sO))
    
    fsum = gsum
    l = 0
    sub = 0
    for i in range(0, n-1):
        sub = arr[l] + arr[l+1]
        l += 2
        gsum = gsum - sub
        (se, so) = getSum(len(arr)+1+1)
        arr.append(abs(se - so))
        gsum += abs(se - so)
        fsum += gsum
    
    esums = 0
    for i in range(0, len(arr)):
        if i % 2 == 0:
            esums += arr[i]
    
    fsum = fsum - esums
    #results.append(esums + 2*fsum)
    #print(arr)
for xx in results:  
    print(xx)   