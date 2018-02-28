
kk = [0,1,2,3,4,5,6,7,8,9]
print(kk)
del kk[1:3]
print(kk)

lday = []
for i in range(0, 10):
    lday.append(i+1)

#print(lday)

def getDay(lday, fd):
    h = len(lday)-1
    l = 0
    if fd > lday[-1]:
        return -1
    while l <= h:
        m = int((l+h)/2)
        if lday[m] < fd:
            l = m+1
        else:
            ans = m
            h = m - 1
    return ans

lday.remove(4)

lday.remove(5)
#print(lday)
d = getDay(lday, 3)
#print(d)
for u in range(d, d + 6):
   #print(u)
    lday.remove(lday[d])
#print(lday)

#print(getDay(lday, 13))