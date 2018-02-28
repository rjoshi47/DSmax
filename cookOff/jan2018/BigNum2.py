'''
Created on 11-Jan-2018

@author: rjoshi
'''
def find3Numbers1(A, arr_size,sum):
    nums = [-1]*3
    # Fix the first element as A[i]
    for i in range( 0,arr_size-2):
 
        # Fix the second element as A[j]
        for j in range(i+1, arr_size-1): 
             
            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is",A[i],
                          ",",A[j],",",A[k])
                    return True
     
    # If we reach here, then no 
    # triplet was found
    return False

def find3Numbers(A, s, e,sum):
    for i in range(s,e):
        for j in range(i+1, e+1): 
            for k in range(j + 1, e+1):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is",A[i],
                          ",",A[j],",",A[k])
                    return True
    return False

a = [1,2,3,4,5,6]
n = len(a)
for i in range(0, int((n*(n+1))/2)):
    print(i)
    find3Numbers(a,0, n-1, i)

# 
# def getPair(arr, s, e, n):
#     nDict = {}
#     for i in range(s, e+1):
#         if arr[i] == n:
#             return (-1, i)
#         elif n - arr[i] in nDict:
#             return (i, nDict[n-arr[i]])
#         else:
#             nDict[arr[i]] = i
#     return (-1, -1)  
# 
# def subSum(w, s, k, r, x, m):
#     msum = 0
#     lp = 0
#     for i in range(0, len(x)):
#         msum += w[i]
#         x[i] = 1
#         if msum >= m:
#             lp = i
#             break
#     extra = msum - m
#     f = 0
#     if extra > 0:
#         for i in range(0, len(x)):
#             if extra == w[i]:
#                 x[i] = 0
#                 f = 1
#                 break
#         if f == 0:
#             (i, j) = getPair(w, extra, s, lp)
#             if i != -1:
#                 x[i] = 0
#             if j != -1:
#                 x[j] = 0
#             
# 
# res = []
# #tests = int(input())
# for zz in range(0, 10000):
#     #(x1, n) = input().split(" ")
#     x1 = zz 
#     n = 10000
#     
#     w = [0]*(n-1)
#     w[0] = 1     
#     if x1 == 1:
#         w[0] = 2  
#     for k in range(1, n-1):
#         if x1 != 1 and k == x1-1:
#             w[k] = w[k-1] + 2
#         else:
#             w[k] = w[k-1] + 1
#     
#     #print(w)
#     msum = int((n*(n+1))/2)
#     msum -= x1
#     if msum % 2 != 0:
#         c = 10
#         #res.append((msum, "impossible"))
#     else:
#         x = [0]*(n-1)
#         subSum(w, 0, 0, msum, x, int(msum/2))
#         fsum = 0
#         for i in range(0, (n-1)):
#             if x[i] == 1:
#                 fsum += w[i]
#         if fsum != int(msum/2):
#             res.append((msum, "impossible"))
#         else:
#             fans = ''
#             for i in range(0, (n-1)):
#                 if i == x1 - 1:
#                     fans += '2'
#                 if x[i] == 1:
#                     fans += '1'
#                 else:
#                     fans += '0'
#             if x1 - 1 == n-1:
#                 fans += '2'
#             #res.append(fans)
#     
# for ii in res:
#     print(ii)
# w = [1,2,3,4,5,6,7,8,9,10]
# 
# x = [0]*len(w)
# subSum(w, 0, 0, 55, x, 30)
# print(x)
