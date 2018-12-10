# 814. Binary Tree Pruning
# https://leetcode.com/problems/binary-tree-pruning/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def go(root):
            if not root: return None
            root.left = go(root.left)
            root.right = go(root.right)
            if not root.left and not root.right and root.val == 0: return None
            return root
            
        go(root)
        return root
