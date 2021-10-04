# https://leetcode.com/problems/binary-tree-cameras/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

IS_NONE = 0
IS_LEAF = 1
IS_SET = 2

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        self.count = 0
        def helper(root):
            if not root:
                return 0

            left_state, right_state = helper(root.left), helper(root.right)

            if left_state == IS_NONE and right_state == IS_NONE:
                return IS_LEAF
            elif left_state == IS_LEAF or right_state == IS_LEAF:
                self.count += 1
                return IS_SET
            elif left_state == IS_SET or right_state == IS_SET:
                # if one of leaf is set, we will take this node as none node
                return IS_NONE


        if helper(root) == IS_LEAF:
            self.count += 1

        return self.count


