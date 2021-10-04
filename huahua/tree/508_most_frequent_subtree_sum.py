# https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:


        self.result = {}
        def helper(root):
            if not root:
                return 0

            if not (root.left or root.right):
                self.result[root.val] = self.result.get(root.val, 0) + 1

                return root.val

            left_val =  helper(root.left)
            right_val =  helper(root.right)

            s = root.val + left_val + right_val
            self.result[s] = self.result.get(s, 0) + 1
            return s

        helper(root)
        max_val = max(self.result.values())

        return [
            k
            for k, v in self.result.items()
            if v == max_val
        ]