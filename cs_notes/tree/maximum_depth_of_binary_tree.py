# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            right_depth = self.maxDepth(root.right) + 1
            left_depth = self.maxDepth(root.left) + 1
            # it seem that using `max` function 
            #   would take more time than if else statement
            return left_depth if left_depth > right_depth else right_depth
