"""543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them."""


# mysol: not correct:  fail case: [3,1,null,null,2]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    lp = [-1, -1]
    def o(self, node, lp):
        print("for", node.val,"lp is", lp)
        r = l = node
        left, right = -1,-1
        while r is not None:
            right += 1
            r = r.right
        while l is not None:
            left += 1
            l = l.left
        print("lp is", lp, "lr are", left, right)
        if lp[0]+lp[1]<left+right:
            lp[0]=left
            lp[1]=right
        print("at end", node.val,"lp is", lp, end='\n\n')
        try:
            self.o(node.left, lp)
        except:
            pass
        try:
            self.o(node.right, lp)
        except:
            pass
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.o(root, self.lp)
        return self.lp[0]+self.lp[1]









"""
The diameter of a tree T is the largest of the following quantities:
1. the diameter of T’s left subtree.
2. the diameter of T’s right subtree.
3. the longest path between leaves that goes through the root of T
   (this can be computed from the heights of the subtrees of T) like, 
   lheight + rheight + 1"""

# The function Compute the "height" of a tree.
# Height is the number of nodes along the longest path from the root node down to the farthest leaf node.
def height(node): 
    # Base Case : Tree is empty
    if node is None:
        return 0
    # else height = 1 + max of left height and right heights
    return 1 + max(height(node.left), height(node.right))

# Function to get the diameter of a binary tree
def diameter(root):
    # Base Case when tree is empty
    if root is None:
        return 0
    # Get the height of left and right sub-trees
    lheight, rheight = height(root.left), height(root.right)
    # Get the diameter of left and right sub-trees
    ldiameter,rdiameter = diameter(root.left), diameter(root.right)
  
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

# Time Complexity: O(n2)








# Optimized implementation: The above implementation can be optimized by calculating the height 
# in the same recursion rather than calling a height() separately.

# utility class to pass height object 
class Height:
    def __init(self):
        self.h = 0
 
# Optimised recursive function to find diameter
# of binary tree
def diameterOpt(root, height):
    # to store height of left and right subtree
    lh = rh = Height()

    # base condition- when binary tree is empty
    if root is None:
        height.h = 0
        return 0
 
    # ldiameter --> diameter of left subtree
    # rdiamter  --> diameter of right subtree
     
    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter

        ldiameter, rdiameter = diameterOpt(root.left, lh), diameterOpt(root.right, rh)
        height.h = max(lh.h, rh.h) + 1
        return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
    
# function to calculate diameter of binary tree
def diameter(root):
    height = Height()
    return diameterOpt(root, height)

# Time Complexity: O(n)








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            self.dia = max(self.dia, left + right)
            
            return max(left, right) + 1
        
        self.dia = 0
        helper(root)
        return self.dia