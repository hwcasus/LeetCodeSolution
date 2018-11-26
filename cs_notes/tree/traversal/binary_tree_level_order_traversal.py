#  Binary Tree Level Order Traversal
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        layer = [root]
        visited = []
        
        while layer:
            next_layer = []
            for curr in layer:
                if curr.left:
                    next_layer.append(curr.left)
                if curr.right:
                    next_layer.append(curr.right)
            
            visited.append([curr.val for curr in layer])
            layer = next_layer    
            
        return visited