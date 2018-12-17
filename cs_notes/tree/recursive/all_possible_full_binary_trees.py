# 894. All Possible Full Binary Trees
# https://leetcode.com/problems/all-possible-full-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        dp = {0:[], 1:[TreeNode(0)]}

        def go(n):
            if n in dp: return dp[n]
            ans = []
            for x in range(n):
                y = (n-1)-x
                for left in go(x):
                    for right in go(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            dp[n] = ans
            return ans
        return go(N)

