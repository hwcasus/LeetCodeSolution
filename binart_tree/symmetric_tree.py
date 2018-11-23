# Symmetric Tree
# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        layer = [root]
        
        while layer:
            next_layer = []
            val = [curr.val if curr else None for curr in layer]
            if val != val[::-1]:
                return False
            
            for curr in layer:
                if not curr:
                    continue
                next_layer.append(curr.left)
                next_layer.append(curr.right)
            
            layer = next_layer    
            
        return True