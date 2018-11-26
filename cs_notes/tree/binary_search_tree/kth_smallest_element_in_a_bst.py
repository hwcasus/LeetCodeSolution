# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """ Use Inorder traversal
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
    
        def inorder(root, cand):
            if not root: return root
            inorder(root.left, cand)
            # This line is critical to stop early
            if len(cand) == k:return
            cand.append(root.val)
            inorder(root.right, cand)
        
        cand = []
        inorder(root, cand)
        return cand.pop()