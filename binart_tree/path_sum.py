# Path Sum
# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.tree_traveler(root, 0, sum) if root else False    
        
        
    def tree_traveler(self, root, curr_sum, goal):
        
        if not root:
            return False
        
        is_leaf = not (root.left or root.right)
        new_sum = curr_sum+root.val
        
        if is_leaf and (new_sum == goal):
            return True
        
        return self.tree_traveler(root.left, new_sum, goal) or self.tree_traveler(root.right, new_sum, goal)

# class Solution:
#     def hasPathSum(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: bool
#         """
#         return self.tree_traveler(root, 0, sum) if root else False    
                
#     def tree_traveler(self, root, curr_sum, goal):
        
#         if not root:
#             return False
        
#         is_leaf = not (root.left or root.right)
#         new_sum = curr_sum+root.val
        
#         if is_leaf and (new_sum == goal):
#             return True
        
#         return self.tree_traveler(root.left, new_sum, goal) or self.tree_traveler(root.right, new_sum, goal)
        