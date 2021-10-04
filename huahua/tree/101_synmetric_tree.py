# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(a, b):
            if a and b:
                return (
                    a.val == b.val
                    and helper(a.left, b.right)
                    and helper(a.right, b.left)
                )
            return a is None and b is None

        if root:
            return helper(root.left, root.right)
        return True


    def isSymmetric_failed(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    queue.append(None)
                    queue.append(None)

            if len(queue) % 2 == 1:
                return False

            if all(n is None for n in queue):
                return True

            for front, end in zip(queue, queue[::-1]):
                if not (front and end):
                    return False
                elif front.val != end.val:
                    return False


        return True