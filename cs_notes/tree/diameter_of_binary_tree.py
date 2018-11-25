# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max = 0
        
        def get_depth(root):
            if not root: return 0

            ld = get_depth(root.left)
            rd = get_depth(root.right)

            
            new_max = ld + rd
            self.max = new_max if self.max < new_max else self.max
            
            return (ld if ld > rd else rd) + 1
        
        get_depth(root)
        return self.max
    
    def diameterOfBinaryTreeNonLocal(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        pmax = 0

        def get_depth(root):
            if not root: return 0

            ld = get_depth(root.left)
            rd = get_depth(root.right)

            nonlocal pmax
            new_max = ld + rd
            pmax = pmax if new_max < pmax else new_max
            
            return (ld if ld > rd else rd) + 1
        
        get_depth(root)        
        return pmax
