# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def helper(root):
            if not root:
                return None

            if key > root.val:
                root.right = helper(root.right)
            elif key < root.val:
                root.left = helper(root.left)
            elif key == root.val:
                succ = root.left
                attach = root.right

                if succ and attach:
                    while succ.right:
                        succ = succ.right

                    succ.right = attach
                    return root.left
                else:
                    return succ or attach

            return root

        return helper(root)