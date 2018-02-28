'''
Created on 07-Feb-2017
http://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/

Everytime we go left that means there is an inversion and all nodes in 
right of current node + current node are greater than this node to be inserted.

count += size(node.right) + 1

@author: rjoshi
'''
def height(node):
    if node is None:
        return -1
    else:
        return node.height

def size(node):
    if node is None:
        return 0
    else:
        return node.size
    
def update_size(node):
    node.size = size(node.left) + size(node.right) + 1 

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1
    
class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0
        self.right = None
        self.left = None
        self.parent = None
        self.height = -1
        self.key = 0
        
    def insert(self, key):
        count = 0
        node = BST()
        node.key = key
        node.size = 1
        if self.root == None:
            self.root = node
        else:
            croot = self.root
            while True:
                if croot.key > key:
                    count += size(croot.right) + 1
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
        print(count)
        return (node, count)
    
    def printT(self):
        if self.left != None:
            self.left.printT()
        print(self.key, end=" ")
        print( self.height, self.size)
        if self.right != None:
            self.right.printT()
           
    def leftRotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x.parent.right is x:
                x.parent.right = y
            if x.parent.left is x:
                x.parent.left = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        x.parent = y
        y.left = x
        update_height(x)
        update_height(y)
        update_size(x)
        update_size(y)
    
    def rightRotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if x.parent.right is x:
                x.parent.right = y
            if x.parent.left is x:
                x.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)
        update_size(x)
        update_size(y)
        
    def rebalance(self, node):
        while node is not None:
            update_height(node)
            update_size(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.rightRotate(node)
                else:
                    self.leftRotate(node.left)
                    self.rightRotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.leftRotate(node)
                else:
                    self.rightRotate(node.right)
                    self.leftRotate(node)
            node = node.parent
    
    def insertAVL(self, t):
        node = self.insert(t)[0]
        self.rebalance(node)
#print("10101".count("1"))
tree = BST()
tree.insertAVL(9)
tree.insertAVL(6)
tree.insertAVL(4)
tree.insertAVL(5)
tree.insertAVL(8)
# tree.insertAVL(4)
# tree.insertAVL(5)
# tree.insertAVL(6)
# tree.insertAVL(7)
# tree.insertAVL(8)
# tree.insertAVL(9)


# tree.insert(5)
# tree.insert(23)
# tree.insert(12)
# tree.insert(21)
# tree.insert(31)
# tree.insert(42)
# tree.insert(41)
# tree.insert(123)
#tree.leftRotate(tree.root.right.right.right.right.right)
#tree.root.printT()    