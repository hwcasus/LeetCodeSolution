# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s, t):
        if not s: return False

        def to_str(n):
            return '^' + str(n.val) + '/' + to_str(n.left) +'\\'+ to_str(n.right) if n else '#'

        return to_str(t) in to_str(s)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return (
            self.is_same(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        ) if root else False

    def is_same(self, p, q):
        if p and q:
            return (
                p.val == q.val
                and self.is_same(p.left, q.left)
                and self.is_same(p.right, q.right)
            )
        return p is None and q is None

