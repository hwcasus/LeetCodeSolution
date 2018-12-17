# 652. Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        這題的想法很特別, 是將 Tree 的轉成字串的感覺
        要注意的是, 如果只是單純轉換成前序或後序
        會發生字串一樣但是架構其實不一樣的狀況
        所以要把 None 的部分也填上, 例如填上 '#' 或是 '.'
        如此一來就可以完整保存當前點作為 root 時的樹的結構
        此外就是用 dict 來記錄每個樹字串出現的次數
        由於輸出只要重複的部份的其中一邊
        所以只需要在出現次數為 2 的時候將其放進 answer
        最後回傳 answer 即可
        """
        d = {}
        ans = []
        def dfs(root):
            if not root: return "."
            key = "{}{}{}".format(root.val, dfs(root.left), dfs(root.right))
            d[key] = d.get(key, 0)+1
            # if d[key] > 1: ans.append(root)
            if d[key] == 2: ans.append(root)
            return key

        dfs(root)
        # print(d)
        return ans
