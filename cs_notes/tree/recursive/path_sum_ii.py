# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if not root: return []
        
        ret = []
        def go(current, root):
            if not root.left and not root.right:
            
                if sum(current)+root.val == s:
                    ret.append(current+[root.val])
            else:
                if root.left:
                    go(current+[root.val], root.left)
                if root.right:
                    go(current+[root.val], root.right)
        
        go([], root)
        return ret
