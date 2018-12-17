# 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        d = {None:-1}
        def dfs(root, parent):
            if not root: return
            d[root] = d[parent]+1
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        # print([(k.val if k else None, v) for k, v in d.items()])

        max_depth = max(d.values())
        def answer(root):
            # 如果走到底或是走到最深的 Node 就回傳
            if not root or d[root] == max_depth: return root
            # 所以這裡的 l 跟 r 一定是最深的點或是 None
            l, r = answer(root.left), answer(root.right)
            # 如果 l 跟 r 都是最深的點, 就表示這個 root 包含了兩個最深的點, 所以回傳 root
            # 但如果這裡只有 l 或 r 那就回傳 l 或 r
            return root if l and r else l or r

        return answer(root)
