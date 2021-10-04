# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.cache = {}

        def helper(root):
            if not root:
                return

            helper(root.left)
            self.cache[root.val] = self.cache.get(root.val, 0) + 1
            helper(root.right)


        helper(root)

        max_count = max(self.cache.values())
        return [
            num for num, count in self.cache.items() if count == max_count
        ]

