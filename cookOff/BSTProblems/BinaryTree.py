'''
Created on 21-Aug-2017

@author: rjoshi
'''
class Node():
    def __init__(self):
        self.num = 0
        self.left = None
        self.right = None
        self.parent = None
        
    
class Btree():
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        node = Node()
        node.num = val
        if self.root == None:
            self.root = node
        else:
            temp = self.root
            while True:
                if temp.num > val:
                    if temp.left == None:
                        temp.left = node
                        node.parent = temp
                        break
                    temp = temp.left
                elif temp.num < val:
                    if temp.right == None:
                        temp.right = node
                        node.parent = temp
                        break
                    temp = temp.right
                    
    def printIN(self, tempRoot):
        if tempRoot == None:
            return
        self.printIN(tempRoot.left)
        print(tempRoot.num)
        self.printIN(tempRoot.right)
            
bTree = Btree()
bTree.insert(30)
bTree.insert(20)
bTree.insert(40)
bTree.insert(10)
bTree.insert(25)
bTree.insert(22)
bTree.insert(35)
bTree.insert(50)
bTree.insert(70)
bTree.insert(38)

#bTree.printIN(bTree.root)
            