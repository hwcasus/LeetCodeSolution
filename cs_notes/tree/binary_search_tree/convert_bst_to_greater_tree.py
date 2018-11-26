# 538. Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def reversed_inorder(root, s):
            if root:
                s = reversed_inorder(root.right, s)
                s += root.val
                root.val = s
                s = reversed_inorder(root.left, s)
            return s
        
        reversed_inorder(root, 0)
        return root
        
    
    def convertBSTBad(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.sum = 0
    
        def reversed_inorder(root):
            if not root: return 0
            reversed_inorder(root.right)
            self.sum += root.val
            root.val = self.sum
            reversed_inorder(root.left)
        
        reversed_inorder(root)
        return root
        