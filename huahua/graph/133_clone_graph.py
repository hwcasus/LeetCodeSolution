class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = dict()

        def traverse(target_node, seen):
            v = target_node.val
            if v in seen:
                return
            else:
                copy_node = Node(v, [])
                seen[v] = copy_node

            for neigh in target_node.neighbors:
                traverse(neigh, seen)
                copy_node.neighbors.append(seen[neigh.val])

            print(copy_node.val, [n.val for n in copy_node.neighbors])

        traverse(node, seen)
        return seen[node.val]

    def cloneGraph(self, node): # DFS recursively
        if not node:
            return node
        m = {node: Node(node.val)}
        self.dfs(node, m)
        return m[node]

    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [Node(2), Node(4)]
    node2.neighbors = [Node(1), Node(3)]
    node3.neighbors = [Node(2), Node(4)]
    node4.neighbors = [Node(1), Node(3)]

    print("node1", id(node1))
    print("node2", id(node2))
    print("node3", id(node3))
    print("node4", id(node4))

    ret = Solution().cloneGraph(node1)
    # Solution().cloneGraph(ret)

    # import ipdb; ipdb.set_trace()