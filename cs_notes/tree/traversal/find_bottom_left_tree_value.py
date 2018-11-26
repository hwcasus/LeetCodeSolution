# 513. Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = [root]
        while queue:
            tmp = []
            for c in queue:
                if c.left: tmp.append(c.left)
                if c.right: tmp.append(c.right)
                    
            if not tmp: return queue[0].val
            queue = tmp