# 951. Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not (root1 or root2): return True
        if bool(root1) ^ bool(root2): return False

        l1 = root1.left.val if root1.left else None
        r1 = root1.right.val if root1.right else None
        l2 = root2.left.val if root2.left else None
        r2 = root2.right.val if root2.right else None

        if l1 == l2 and r1 == r2:
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if l1 == r2 and r1 == l2:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

        return False
