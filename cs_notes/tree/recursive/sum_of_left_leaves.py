# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0
        if self.is_leaf(root.left): return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        
    def is_leaf(self, root):
        if not root:return False
        return not root.left and not root.right
    
    
    def sumOfLeftLeavesMe(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ll_sum = 0
        def traveler(root, is_left):
            if root:
                if not root.left and not root.right and is_left:
                    nonlocal ll_sum
                    ll_sum += root.val
                if root.left: traveler(root.left, True)
                if root.right: traveler(root.right, False)

        traveler(root, False)
        return ll_sum
                
            