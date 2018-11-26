# 337. House Robber III
# https://leetcode.com/problems/house-robber-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return max(*self.rob_sub(root))
        
    def rob_sub(self, root):
        if not root: return (0, 0)
        
        l_self, l_child = self.rob_sub(root.left)
        r_self, r_child = self.rob_sub(root.right)
        
        return (root.val+l_child+r_child, max(l_self, l_child) + max(r_self, r_child))
        # My original way, which forget to choose the best not-picking-self-var way (second element)
        # return (root.val+l_child+r_child, l_child + r_child) 
        
        
        
    def rob_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return root.val
        
        val1 = root.val
        if root.left: val1 = val1 + self.rob_recursive(root.left.left) + self.rob_recursive(root.left.right)
        if root.right: val1 = val1 + self.rob_recursive(root.right.left) + self.rob_recursive(root.right.right)
        
        val2 = self.rob_recursive(root.left) + self.rob_recursive(root.right)
        return max(val1, val2)
        
        
        