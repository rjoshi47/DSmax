'''
Created on 18-Dec-2017

@author: rjoshi

The idea was to fix each character from the beginning and print space separated rest of the string.
Like for "ABCD": 
A BCD # Fix A and print rest string
AB CD # Add B to previous value A and print rest of the string
ABC D # Add C to previous value AB and print rest of the string
Similarly we can add a space to produce all permutations.
Like:
In second step above we got "AB CD" by having "A" as prefix
So now we can get "A B CD" by having "A " as a prefix
'''

def printPermute(arr, s, app):
    if len(arr) <= 1:
        return 
    else:
        print(app + ''+arr[0:s] +' '+ arr[s:len(arr)])
        prefix = app + ''+arr[0:s]
        suffix = arr[s:len(arr)]
        printPermute(suffix, 1, prefix)
        printPermute(suffix, 1, prefix+' ')
       
        

         
arr = "ABCD"
#for i in range(1, len(arr)):
printPermute(arr, 1, '')
#test2(arr, len(arr)-1, '')
