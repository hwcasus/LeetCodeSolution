# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.node = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.node.append(root.val)
            inorder(root.right)

        inorder(root)
        return self.node[k-1]