'''
Created on 07-Jul-2017

@author: rjoshi
'''
results = []
tests = int(input())
for i in range(0, tests):
    chars = input().split(" ")
    if len(chars) == 1:
        st1 = chars[0]
        l = len(st1)
        if l == 1:
            results.append(st1[0:1].upper())
        else:
            results.append(st1[0:1].upper()+st1[1:l].lower())
    elif len(chars) == 2:
        st1 = chars[0]
        st2 = chars[1]
        fstr = st1[0:1].upper()+". "
        l = len(st2)
        if l == 1:
            fstr = fstr + st2[0:1].upper()
        else:
            fstr = fstr + st2[0:1].upper()+st2[1:l].lower()
        results.append(fstr)
    elif len(chars) == 3:
        st1 = chars[0]
        st2 = chars[1]
        st3 = chars[2]
        fstr = st1[0:1].upper()+". "
        fstr = fstr + st2[0:1].upper()+". "
        
        l = len(st3)
        if l == 1:
            fstr = fstr + st3[0:1].upper()
        else:
            fstr = fstr + st3[0:1].upper()+st3[1:l].lower()
        results.append(fstr)    
    
for xx in results:
    print(xx)