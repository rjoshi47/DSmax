'''
Created on 12-Oct-2017

@author: rjoshi
'''
def myCompare(num1, num2):
    if int(str(num1)+str(num2)) > int(str(num2)+str(num1)):
        return 1
    else:
        return 0
    
arr = [54, 546, 548, 60]
sorted(arr, key=lambda x, y: myCompare(x,y))
print(arr)
    