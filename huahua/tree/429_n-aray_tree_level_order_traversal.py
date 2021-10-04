# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return

        curr_level = [root]
        visited = []

        while curr_level:
            level_visited = []

            for _ in range(len(curr_level)):
                curr = curr_level.pop(0)
                level_visited.append(curr.val)
                curr_level.extend(curr.children)

            visited.append(level_visited)

        return visited

    def levelOrder_v1(self, root: 'Node') -> List[List[int]]:
        if not root:
            return

        curr_level = [root]
        next_level = []
        visited = []


        while curr_level:
            level_visited = []
            while curr_level:
                curr = curr_level.pop()
                level_visited.append(curr.val)

                if curr.children:
                    next_level.extend(curr.children)

            visited.append(level_visited)
            curr_level, next_level = next_level[::-1], curr_level

        return visited