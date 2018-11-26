# 687. Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.length = 0
        
        def traveler(root):
            if not root: return 0
            
            l, r = traveler(root.left), traveler(root.right)
            llen = (l + 1) if (root.left and root.left.val == root.val) else 0
            rlen = (r + 1) if (root.right and root.right.val == root.val) else 0
            
            self.length = max(self.length, llen + rlen)
            return max(llen, rlen)
        
        traveler(root)
        return self.length