# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pace = []

        if root:
            def helper(subroot):
                if subroot.left:
                    helper(subroot.left)
                pace.append(subroot.val)
                if subroot.right:
                    helper(subroot.right)
            helper(root)

        return pace
