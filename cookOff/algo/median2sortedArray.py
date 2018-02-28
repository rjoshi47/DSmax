'''
Created on 07-May-2017

@author: rjoshi
'''
def getMedian(arr1, arr2, s1, e1, s2, e2):
    print()  
    for a in range(s1, e1+1):
        print(str(arr1[a])+" ", end="")
    
    print()    
    
    for b in range(s2, e2+1):
        print(str(arr2[b])+" ", end="")
        
    print() 
    
    
    l1 = e1 - s1
    l2 = e2 - s2
    if l1 == 1 and l2 == 1:
        return (max(arr1[s1], arr2[s2]) + min(arr1[e1], arr2[e2]))/2
    elif l1 == 0 and l2 == 1:
        return min(max(arr1[s1], arr2[s2]), arr2[e2])
    elif l1 == 1 and l2 == 0:
        return min(max(arr1[s1], arr2[s2]), arr1[e1])
    
    
    m1 = int((s1 + e1)/2)
    m2 = int((s2 + e2)/2)
    
    m1v = arr1[m1]
    m2v = arr2[m2]
   
            
    if m1v < m2v:
        s1 = m1
        if l1 == l2 and l2 % 2 != 0:
            e2 = m2 + 1
        else:
            e2 = m2
        if l2 > l1:
            s1 = s1 + 1
    else:
        s2 = m2
        if l1 == l2 and l1 % 2 != 0:
            e1 = m1 + 1
        else:
            e1 = m1
        if l1 > l2:
            s2 = s2 + 1
    
        
        
    return getMedian(arr1, arr2, s1, e1, s2, e2)


print(getMedian( [5,8,11,12,13,14,15,16,18,20,21],[1,2,3,4,6,7,9,10,17,19]
                , 0, 10, 0, 9))