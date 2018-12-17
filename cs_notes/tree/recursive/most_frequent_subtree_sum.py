# 508. Most Frequent Subtree Sum
# https://leetcode.com/problems/most-frequent-subtree-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        本題想法來自於 652. Find Duplicate Subtrees
        其中使用字典並將樹結構轉換成字串作為 key 進行計數, 並以此來偵測重複結構
        本題是使用當前總和作為 key, 以記錄重複出現的總和值
        此外使用了 nonlocal 以方便更新, 也可以直接使用 Counter, 應該會更輕鬆
        """
        d = {}
        count = 0
        ans = []

        def dfs(root):
            if not root: return 0
            sum_here = root.val + dfs(root.left) + dfs(root.right)
            d[sum_here] = d.get(sum_here, 0) + 1
            nonlocal count, ans
            if d[sum_here] > count:
                count = d[sum_here]
                ans = [sum_here]
            elif d[sum_here] == count:
                ans += [sum_here]
            return sum_here

        dfs(root)
        return ans
