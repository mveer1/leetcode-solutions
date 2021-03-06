#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return 
        if val==root.val:
            return root
        elif val<root.val:
            return self.searchBST(root.left, val)
        elif val>root.val:
            return self.searchBST(root.right, val)
# @lc code=end

