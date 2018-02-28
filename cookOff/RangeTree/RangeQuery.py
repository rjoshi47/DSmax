'''
Created on 17-Jun-2017

@author: rjoshi
'''

def buildImpl(nums, tree, i, l, r, c):
    print(c)
    if l == r:
        tree[i] = nums[l]
    else:
        m = int((l+r)/2)
        buildImpl(nums, tree, 2*i, l, m, c+1)
        buildImpl(nums, tree, 2*i + 1, m+1, r, c+1)
        tree[i] = tree[2*i] + tree[2*i + 1]
        
def build(nums):
    size = len(nums)
    tree = [0]*(4*size)
    buildImpl(nums, tree, 1, 0, size-1, 0)
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

def update(tree, ui, val, i, l, r):
    if l == r:
        tree[i] = val
        return
    else:
        m = int((l+r)/2)
        if ui <= m:
            update(tree, ui, val, 2*i, l, m)
        else:
            update(tree, ui, val, 2*i+1, m+1, r)
    tree[i] = tree[2*i] + tree[2*i + 1]
    
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
    
    

nums = [1,1,1,1,1,1,1]
tree = build(nums)

#[1,0,0,0,0,1,1]
updateOnes(tree, 1, 4, 1, 0, len(nums)-1)
#[1,0,1,1,1,0,1]
updateOnes(tree, 2, 5, 1, 0, len(nums)-1)
#[1,0,0,0,0,0,1]
updateOnes(tree, 2, 4, 1, 0, len(nums)-1)
# print(getSum(tree, 0, 2, 1, 0, len(nums)-1))
# print(getSum(tree, 1, 4, 1, 0, len(nums)-1))
# print(getSum(tree, 3, 7, 1, 0, len(nums)-1))
# print(getSum(tree, 0, 7, 1, 0, len(nums)-1))