# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """ Idea of this problem is that travel to the node whose val is between p and q
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Since all value is somehow sorted
        # we go left if current val is too big, go right if too small
        if root.val < p.val and root.val < q.val: return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val and root.val > p.val: return self.lowestCommonAncestor(root.left, p, q)
        return root