'''
Created on 13-Mar-2017

@author: rjoshi
'''

class BST(object):
    def __init__(self):
        self.root = None
        self.right = None
        self.left = None
        self.parent = None
        self.key = 0
        self.i = 0
        self.j = 0
        self.sum = 0
    
    def printT(self):
        if self.left != None:
            self.left.printT()
        print(self.i, self.j, self.sum)
        if self.right != None:
            self.right.printT()
    
    def makeTreeImpl(self, l, h):
        self.makeTree(l, h)
        if h-l > 0:
            mid = int((h+l)/2)
            self.makeTreeImpl(l, mid)    
            self.makeTreeImpl(mid+1, h)
            
    def makeTree(self, low, high):
        #print(low, high)
        node = BST()
        node.i = low
        node.j = high
        if self.root == None:
            self.root = node
        else:
            croot = self.root
            while True:
                cmid = int((croot.j + croot.i)/2)
                if high <= cmid:
                    if croot.left == None:
                        croot.left = node
                        node.parent = croot
                        break
                    else:
                        croot = croot.left
                else:
                    if croot.right == None:
                        croot.right = node
                        node.parent = croot
                        break
                    else:
                        croot = croot.right
        return node
    
    def propagateSumToRoot(self,rootNode, node):
        while node.parent != rootNode:
            node = node.parent
            l = 0
            r = 0
            if node.left != None:
                l = node.left.sum
            if node.right != None:
                r = node.right.sum
            node.sum = r + l
            
        
    def findRangeSum(self, node, sl, sh):
        if sl <= node.i and sh >= node.j:
            return node.sum
        else:
            mid = int((node.i + node.j)/2)
            if mid >= sh:
                return self.findRangeSum(node.left, sl, sh)
            elif mid < sl:
                return self.findRangeSum(node.right, sl, sh)
            else:
                return self.findRangeSum(node.left, sl, mid) + self.findRangeSum(node.right, mid+1, sh)
    
    def updateRange(self, node, sl, sh):
        if node.i == node.j:
            if node.sum == 0:
                node.sum = 1
            else:
                node.sum = 0
            self.propagateSumToRoot(None, node)
        else:
            mid = int((node.i + node.j)/2)
            if mid >= sh:
                self.updateRange(node.left, sl, sh)
            elif mid < sl:
                self.updateRange(node.right, sl, sh)
            else:
                self.updateRange(node.left, sl, mid)
                self.updateRange(node.right, mid+1, sh)
    
             
#      
# bst = BST()
# bst.makeTreeImpl(0, 8)
# #bst.root.printT()
# bst.root.updateRange(bst.root, 4, 8)
# #bst.root.printT()
# print(bst.root.findRangeSum(bst.root, 4, 8))
# print(bst.root.findRangeSum(bst.root, 2, 7))
# bst.root.updateRange(bst.root, 6, 7)
# print(bst.root.findRangeSum(bst.root, 4, 8))
# print(bst.root.findRangeSum(bst.root, 2, 7))
# bst.root.updateRange(bst.root, 5, 8)
# print(bst.root.findRangeSum(bst.root, 4, 8))
# print(bst.root.findRangeSum(bst.root, 2, 7))
#bst.root.printT()
#print(bst.root.findRangeSum(bst.root, 4, 8))
#bst.root.updateRange(bst.root, 4, 8)
#bst.root.printT()
#print(bst.root.findRangeSum(bst.root, 4, 8))
results = []
(n, m) = input().split(" ")
bst = BST()
bst.makeTreeImpl(0, int(n)-1)
for c in range(0, int(m)):
    (i, j, k) = input().split(" ")
    if i == '1':
        results.append(bst.root.findRangeSum(bst.root, int(j), int(k)))
    else:
        bst.root.updateRange(bst.root, int(j), int(k))
  
for xx in results:
    print(xx)