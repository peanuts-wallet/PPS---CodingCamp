class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, None)]

        while queue:
            level_size = len(queue)
            parents = {}

            for _ in range(level_size):
                node, parent = queue.pop(0)

                if node.val == x or node.val == y:
                    parents[node.val] = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if x in parents or y in parents:
                return x in parents and y in parents and parents[x] != parents[y]

        return False
