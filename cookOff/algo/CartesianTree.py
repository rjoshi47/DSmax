'''
Created on 23-Jul-2017

@author: rjoshi
'''

class CTree():
    def __init__(self):
        self.root = None
        self.iNode = None
    
    def setINode(self, node):
        self.iNode = node
        
    def getINode(self):
        return self.iNode
    
    def setRoot(self, node):
        self.root = node
        
    def getRoot(self):
        return self.root
    
class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None
        
def insert(CTree, Node):
    if CTree.getRoot() == None:
        CTree.setRoot(node)
        CTree.setINode(node)
    else:
        iNode = CTree.getINode()
        root = CTree.getRoot()
        while iNode.val < node.val and iNode != root:
            iNode = iNode.parent
        if iNode == root:
            if node.val > root.val:
                rRight = root.right
                if rRight == None:
                    node.parent = root
                    CTree.setINode(node)
                    root.right = node
                else:
                    root.right = node
                    node.parent = root
                    node.left = rRight
                    rRight.parent = node
            else:
                node.left = root
                node.right = root.right
                if root.right != None:
                    root.right.parent = node
                root.parent = node
                CTree.setRoot(node)
                CTree.setINode(node)
        else:
            if node.val > iNode.val:
                
        
        

node = Node(10)
node.left = Node(20)
print(node.left.val)


        