'''
Created on 20-Dec-2017

@author: rjoshi
'''
# cook your dish here

def getNumber(gsum, gdigits):
    if (gdigits == 1 and gsum > 9) or (gsum > 9*gdigits):
        return -1
    myNumber = []
    for i in range(gdigits):
        if gsum == 0:
            if gdigits > 0:
                myNumber += [0]*gdigits
            break
        
        if i == 0:
            # In case of 20 in 3 digit -> 299
            if gsum - 1 > 9*(gdigits - 1):
                myNumber.append(gsum - 9*(gdigits - 1))
                myNumber += [9]*(gdigits - 1)
                break
            else:
                # In case of 10 in 2 digits 19
                myNumber.append(1)
                gsum -= 1
                gdigits -= 1
        else:
            if gsum > 9*(gdigits - 1):
                myNumber.append(gsum - 9*(gdigits - 1))
                myNumber += [9]*(gdigits - 1)
                break
            else:
                myNumber.append(0)
                gdigits -= 1
    return myNumber

print(getNumber(23, 6))
