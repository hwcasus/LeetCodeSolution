# 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        這裡的想法跟我一樣
        不同的是
        1) fake root 的想法, 如此就可以避免 d = 1 要寫例外狀況的處理
        2) 只取到要被取代的層的上一層, 下稱 last
           然後將新的一層接在 last 下面, 把 last 的左右孩子再往下接
           原本以為這樣會有 None 的問題要處理, 但好像不會
           因為如果 Node 沒有在 last 就不會往下接
           如果 Node 在 last 中, 就代表一定有孩子可以存取,
           至於孩子到底是 None 還是 TreeNode 都不影響程式運作
        """
        if not root: return root

        fake_root = TreeNode(None)
        fake_root.left = root
        queue = [fake_root]

        for i in range(d-1):
            for j in range(len(queue)):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        for node in queue:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right

        return fake_root.left

    def addOneRowSlow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        這邊的想法是
        用 BFS 走到要被取代的層, 並記錄上一層
        然後依序將新增層和上一層跟下一層接起來
        但超時了
        """

        if not root: return root
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        curr = [root]
        last = []
        for i in range(d-1):
            last = []
            for j in range(len(curr)):
                node = curr.pop(0)
                if node:
                    curr.append(node.left)
                    curr.append(node.right)
                else:
                    curr.append(None)
                    curr.append(None)
                last.append(node)

        for i, node in enumerate(last):
            if node:
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                node.left.left = curr[2*i]
                node.right.right = curr[2*i+1]


        return root
