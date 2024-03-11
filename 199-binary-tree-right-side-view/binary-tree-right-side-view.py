class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = [ ]
        queue = [root]
        level = [ ]

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

# O(N)  TIME
# O(1) SPACE

