'''
Created on 06-Nov-2017

@author: rjoshi
'''
def isPalin(sss):
    l = 0
    r = len(sss) - 1
    while l <= r:
        if sss[l] != sss[r]:
            return False
        l += 1
        r -= 1 
    return True

def test(n, p):
    print(n, end=" ")
    print(p)
    if p == 1 or p == 2 or n == 1:
        print("impossible")
    elif n == p:
        pal = ""
        c = n - 2
        pal = 'a'
        while c > 0:
            pal += 'b'
            c -= 1
        pal += 'a'
        print(pal, end=", ")
        print(len(pal), end= " ")
        print(isPalin(pal))
        
    else:
        m = int(n/p) - 1
            
        pal = ""
        c = p - 2
        pal = 'a'
        while c > 0:
            pal += 'b'
            c -= 1
        pal += 'a'
        
        palf = pal
        while m > 0:
            palf += pal
            m -= 1
            
        print(palf, end=", ")
        print(len(palf), end= " ")
        print(isPalin(pal))

num = 12
for i in range(1, num+1):
    test(num , i)
    
    