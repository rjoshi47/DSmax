'''
Created on 18-Jun-2017

@author: rjoshi
'''
def buildImpl(nums, tree, i, l, r):
    if l == r:
        tree[i] = nums[l]
    else:
        m = int((l+r)/2)
        buildImpl(nums, tree, 2*i, l, m)
        buildImpl(nums, tree, 2*i + 1, m+1, r)
        tree[i] = tree[2*i] + tree[2*i + 1]
        
def build(nums):
    size = len(nums)
    tree = [0]*(4*size)
    buildImpl(nums, tree, 1, 0, size-1)
    return tree

def getSum(tree, a, b, i, l, r):
    if a <= l and b >= r:
        return tree[i]
    elif l > b or r < a:
        return 0
    else:
        m = int((l+r)/2)
        return (getSum(tree, a, b, 2*i, l, m) + 
                getSum(tree, a, b, 2*i+1, m+1, r))

    
def updateOnes(tree, s1, e1, i, l, r):
    if l == r and (s1 <= l and l <= e1):
        if tree[i] == 1:
            tree[i] = 0
        else:
            tree[i] = 1
        return
    else:
        m = int((l+r)/2)
        if s1 <= m:
            updateOnes(tree, s1, e1, 2*i, l, m)
        if e1 > m:
            updateOnes(tree, s1, e1, 2*i+1, m+1, r)
    tree[i] = tree[2*i] + tree[2*i + 1]
    
(n, q) = input().split(" ")
nums = [0]*int(n)
tree = build(nums)
results = []
for i in range(0, int(q)):
    que = input().split(" ")
    c = que[0]
    if c == '0':
        updateOnes(tree, int(que[1]), int(que[2]), 1, 0, int(n)-1)
    if c == '1':
        results.append(getSum(tree, int(que[1]), int(que[2]), 1, 0, int(n)-1))
for xx in results:
    print(xx)