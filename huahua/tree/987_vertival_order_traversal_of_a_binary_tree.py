# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [(0, root)]
        visited = defaultdict(list)

        while queue:
            size = len(queue)
            queue.sort(key=lambda p: (p[0], p[1].val))
            for _ in range(size):
                column, curr = queue.pop(0)
                visited[column].append(curr.val)

                if curr.right:
                    queue.append((column + 1, curr.right))

                if curr.left:
                    queue.append((column - 1, curr.left))


        columns = visited.keys()
        visit_list = [
            visited[i]
            for i in range(min(columns), max(columns) + 1)
            if visited[i]
        ]

        return visit_list