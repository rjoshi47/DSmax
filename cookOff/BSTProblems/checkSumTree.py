'''
Created on 01-Jan-2018

@author: rjoshi
'''

from BSTProblems.BinaryTree import Node
def isSumTree(node):
    if node is None:
        return True
    elif node.right != None and node.left != None:
        if node.num != node.left.num + node.right.num:
            return False
        else:
            return isSumTree(node.left) and isSumTree(node.right)
    elif node.right != None:
        if node.num != node.right.num:
            return False
        else:
            return isSumTree(node.right)
    elif node.left != None:
        if node.num != node.left.num:
            return False
        else:
            return isSumTree(node.left)
    else:
        return True

node10 = Node()
node10.num = 10

node20 = Node()
node20.num = 20

node15 = Node()
node15.num = 15

node25 = Node()
node25.num = 25

node30 = Node()
node30.num = 30
node30.left = node10
node30.right = node20

node40 = Node()
node40.num = 40
node40.left = node15
node40.right = node25


node70 = Node()
node70.num = 70
node70.left = node30
node70.right = node40

print(isSumTree(node70))