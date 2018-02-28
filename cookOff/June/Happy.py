'''
Created on 08-Jun-2017

@author: rjoshi
'''   
def max_subarray(A):
    max_so_far = max_ending_here = int(A[0])
    s = 0
    e = 0
    c = 1
    msum = 0
    temp_start_index = temp_end_index = 0
    for i in range(1, len(A)):
        #temp_start_index = temp_end_index = None
        print(c)
        if int(A[i]) > (max_ending_here + int(A[i]))*(temp_end_index - temp_start_index + 2):
            msum = msum + max_ending_here*(temp_end_index - temp_start_index + 1)
            temp_start_index = temp_end_index = i
            max_ending_here = int(A[i])
            print("#",A[i])
            c = 1
        else:
            temp_end_index = i
            max_ending_here = max_ending_here + int(A[i])
            c = c + 1
        if max_so_far < max_ending_here:     
            max_so_far = max_ending_here
            if temp_start_index != None:
                s = temp_start_index
            e = i
    print(s,e)
    sum0 = 0
    for n in range(0, s):
        sum0 = sum0 + int(A[n])
     
    sum1 = 0
    for n in range(s, e+1):
        sum1 = sum1 + int(A[n])
    sum0 = sum0 + int(sum1*(e-s+1))
     
    sum2 = 0
    for n in range(e+1, len(A)):
        sum2 = sum2 + int(A[n])
    sum0 = sum0 + sum2
     
    return sum0
             
print(max_subarray([1,-1,2,-10,2,-1,2]))
# print(max_subarray([-1,2,3,-4]))
# print(max_subarray([1,-2,3,-4]))
# print(max_subarray([-1,-2,3,-1]))
# print(max_subarray([1,-2,-3,-4]))
