# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def max_depth(self, root):
            if not root: return 0
            
            l_d = self.max_depth(root.left)
            r_d = self.max_depth(root.right)

            if l_d == -1 or r_d == -1 or abs(l_d - r_d) >= 2: return -1
            return (l_d if l_d > r_d else r_d) + 1
            
        return self.max_depth(root) != -1
    
    def isBalancedEasy(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.c = True
        
        def max_depth(self, root):
            if not root: return 0

            l_d = self.max_depth(root.left)
            r_d = self.max_depth(root.right)

            if self.c: self.c = abs(l_d - r_d) < 2
            return (l_d if l_d > r_d else r_d) + 1
            
        self.max_depth(root)
        return self.c
        
    

