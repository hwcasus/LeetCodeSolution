# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.res = []
        def helper(root, carry):
            carry.append(str(root.val))
            if not (root.left or root.right):
                ans = carry[0] if len(carry) == 1 else "->".join(carry)
                self.res.append(ans)
            else:
                if root.left:
                    helper(root.left, carry)
                if root.right:
                    helper(root.right, carry)

            carry.pop()

        helper(root, [])
        return self.res