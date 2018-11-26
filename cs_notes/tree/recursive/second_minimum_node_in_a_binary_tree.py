# 671. Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.f_min = root.val
        def findSecondMinimumValueAct(root):
            if not root: return []
            cand = [root.val] if root.val > self.f_min else []
            return cand + findSecondMinimumValueAct(root.left) + findSecondMinimumValueAct(root.right)
        
        cand = findSecondMinimumValueAct(root)
        return min(cand) if cand else -1
                
        
    def findSecondMinimumValueIterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return -1
        
        queue = [root]
        f_min = root.val
        cand = []
        
        while queue:
            tmp = []
            for c in queue:
                if c.val > f_min: cand.append(c.val)
                if c.left: tmp.append(c.left)
                if c.right: tmp.append(c.right)
                    
            queue = tmp
        
        return min(cand) if cand else -1
            