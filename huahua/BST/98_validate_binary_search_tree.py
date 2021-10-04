# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(root):
            if not root:
                return True

            if not inorder(root.left):
                return False

            if root.val <= self.prev:
                return False

            self.prev = root.val

            return inorder(root.right)

        self.prev = float('-inf')
        return inorder(root)


    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root.left and not root.right:
                return (True, root.val, root.val)

            is_valid = True
            curr_min = curr_max = root.val
            if root.left:
                is_left_valid, left_min, left_max = helper(root.left)
                is_valid = is_valid and is_left_valid and (left_max < root.val)
                curr_min = left_min

            if root.right:
                is_right_valid, right_min, right_max = helper(root.right)
                is_valid = is_valid and is_right_valid and (right_min > root.val)
                curr_max = right_max

            return is_valid, curr_min, curr_max

        return helper(root)[0]


