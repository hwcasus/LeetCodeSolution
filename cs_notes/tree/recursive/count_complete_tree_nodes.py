# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        def get_depth(root):
            if not root: return 0
            return 1+get_depth(root.left)
        
        ld, rd = get_depth(root.left), get_depth(root.right)
        if ld==rd:
            # 如果兩邊一樣深，代表說左邊是完美二元樹, Node 數 = 2**深度 -1
            # 所以數量會變成 (root) + 完美的左邊子樹 + 繼續算出來的右子樹
            return 1 + (pow(2, ld)-1) + self.countNodes(root.right)
        else:
            return 1 + (pow(2, rd)-1) + self.countNodes(root.left)
        
    def countNodesSlow2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def go(root, c):
            if not root: return 0
            if not (root.left or root.right): return c
            return max(go(root.right, 2*c+1) if root.right else 0, go(root.left, 2*c) if root.left else 0)
        
        return go(root, 1)
        
    def countNodesSlow(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: return 0
        cnt = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                curr = queue.pop()
                cnt += 1
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        
        return cnt
