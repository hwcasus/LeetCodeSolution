# 863. All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        這題有兩種解法
        2) Recursion
            要往三個方向探索
            a) target 的子樹
            b) 和 target 同側, 但是但比 target 更靠近 root 的部分
            c) 和 target 不同側
            a 的情況就只要找出用 dfs 找出離 target 距離為 k 的點就好
            而 b, c 情況套用同一種解法, 往下看吧
        """
        ans = []
        def go(root, d):
            if not root or d < 0: return
            if d == 0: ans.append(root.val)
            go(root.left, d-1)
            go(root.right, d-1)


        def dfs(root):
            if not root: return -1
            if root == target:
                go(root, K)
                return 0 # 會回傳到上一層的 l, r 中
            l, r = dfs(root.left), dfs(root.right)
            # print(root.val, l, r)

            # 以下設計為 l+1 = target 到 root 的距離
            # 如果是 0 表示該側子葉就是 target
            if l >= 0:
                # 如果 l+1 == K 表示自己跟 target 距離就是 K
                if (l+1==K): ans.append(root.val)
                # 只要 l >= 0 就表示 target 在左側, 也就表示如果要往自己右側尋找的話
                # 必須要從 target -> ... -> root -> root.right 開始找
                # 而 l+1 就是 target 到 root 距離, 所以 l+1 再加上 root -> root.right 的距離
                # 就是 l+2, 而剩下可用的距離就是 k-(l+2)
                go(root.right, K-(l+1+1))
                # 最後回傳 l+1 到上一層的 root, 就會去找 root 的另外一個孩子
                return l + 1
            if r >= 0:
                if (r+1==K): ans.append(root.val)
                go(root.left, K-(r+1+1))
                return r + 1
            return -1

        dfs(root)
        return ans

    def distanceK2(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        這題有兩種解法
        1) DFS + BFS
            DFS 將 Tree 轉為無向圖 (新增一變數紀錄自己的 parent node)
            BFS 從 target 開始往外走 K 步, 因為可以往 parent node 走, 所以沒問題
        """

        def dfs(root, p):
            if not root: return
            root.parent = p
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        queue = [target]
        visited = set()
        visited.add(target)

        for i in range(K):
            for i in range(len(queue)):
                curr = queue.pop(0)
                for node in [curr.left, curr.right, curr.parent]:
                    if node and node not in visited:
                        queue.append(node)
                        visited.add(node)
        return [node.val for node in queue]


