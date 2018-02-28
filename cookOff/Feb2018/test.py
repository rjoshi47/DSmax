'''
Created on 03-Feb-2018

@author: rjoshi
'''

print((33333/179)*999)

c = (33333/179)
s = c
for i in range(0, 998):
    s += c
print(s)