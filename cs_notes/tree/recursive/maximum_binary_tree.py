# 654. Maximum Binary Tree
# https://leetcode.com/problems/maximum-binary-tree/description/

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if not nums: return None
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root
