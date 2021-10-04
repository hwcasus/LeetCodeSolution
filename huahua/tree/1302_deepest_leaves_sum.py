# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        while queue:
            size = len(queue)
            level_sum = 0
            for _ in range(size):
                curr = queue.pop(0)
                level_sum += curr.val

                if curr.right:
                    queue.append(curr.right)

                if curr.left:
                    queue.append(curr.left)

        return level_sum

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            pre, q = q, [i for p in q for i in [p.left, p.right] if i]
        return sum([i.val for i in pre])