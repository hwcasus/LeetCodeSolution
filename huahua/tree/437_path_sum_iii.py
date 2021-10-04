# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.result = 0
        self.so_far = 0
        self.cache = {0: 1}

        def helper(root):
            if not root:
                return

            self.so_far += root.val
            self.result += self.cache.get(self.so_far - targetSum, 0)
            self.cache.setdefault(self.so_far, 0)

            self.cache[self.so_far] += 1
            helper(root.left)
            helper(root.right)
            self.cache[self.so_far] -= 1
            self.so_far -= root.val

        helper(root)
        return self.result


    def pathSumSoBad(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(root):
            if not root:
                return [], []

            left_mov, left_fix = helper(root.left)
            right_mov, right_fix = helper(root.right)

            fix = left_mov + left_fix + right_mov + right_fix
            mov = [0] + left_mov + right_mov
            mov = [e + root.val for e in mov]

            return mov, fix

        mov, fix = helper(root)

        return sum(e == targetSum for e in (mov + fix))
