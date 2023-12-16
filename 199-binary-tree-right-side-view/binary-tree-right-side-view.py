class Solution(object):
    def rightSideView(self, root):

        if not root:
            return []

        result = []
        level = []
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

# O(N) Time and Space