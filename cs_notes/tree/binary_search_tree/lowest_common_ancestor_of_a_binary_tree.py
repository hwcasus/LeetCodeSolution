# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if (not root) or (root.val == p.val) or (root.val == q.val): return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If the current (sub)tree contains both p and q, then the function result is their LCA. 
        # If only one of them is in that subtree, then the result is that one of them. 
        # If neither are in that subtree, the result is null/None/nil.       
        return root if left and right else (left or right)