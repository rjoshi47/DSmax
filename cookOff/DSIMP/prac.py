def max_subarray(A):
# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane%27s_algorithm_(Algorithm_3:_Dynamic_Programming)
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def maxR(A):
    cm = sum_so_far = A[-1:]
    for i in range(0, len(A))[::-1]:
        sum_so_far = sum_so_far + A[i]
        cm = max(cm, sum_so_far)
    return cm

def maxL(A):
    cm = sum_so_far = A[0]
    for i in range(0, len(A)):
        sum_so_far = sum_so_far + A[i]
        cm = max(cm, sum_so_far)
    return cm

def max_subarray_rep(A,k):
    sumS=max_subarray(A)
    if(k<1):
        return sumS
    sumL=maxL(A)
    sumR=maxR(A)
    if(k==1):
        return max(sumS, sumR+sumL)
    sumT=sum(A)
    sumLong = (k-1)*sumT + max(0, sumL) + max(0, sumR)
    return max(sumLong, sumR+sumL, sumS)

print(max_subarray_rep([-5,2,2,2,-5,2,2,2], 1))