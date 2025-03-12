# Travel the tree level by leve.
# How do we keep track of the node?
# Should I use stack or queue. DFS OR BFS. Since it's level by level. Then it's BFS:
# Use a qeue = FIFO = pop nodes
# 
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        level = []
        result = []
        queue = [root]

        while queue:
            for node in queue:
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            result.append(node.val)
            queue = level
            level = []

        return result

# O(N) time and space

        