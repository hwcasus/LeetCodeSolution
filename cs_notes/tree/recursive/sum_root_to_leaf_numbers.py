# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root: return 0
        ret = []
        def dfs(root, num):
            num = num * 10 + root.val
            if not root.left and not root.right: ret.append(num)
            if root.left: dfs(root.left, num)
            if root.right: dfs(root.right, num)

        dfs(root, 0)
        return sum(ret)
