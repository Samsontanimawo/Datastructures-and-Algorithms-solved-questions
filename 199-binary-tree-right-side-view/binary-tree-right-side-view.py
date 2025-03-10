class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        nextLevel = []
        queue = [root]

        while queue and root != None:
            for node in queue:
                if node.left:
                    nextLevel.append(node.left)

                if node.right:
                    nextLevel.append(node.right)

            result.append(node.val)
            queue = nextLevel
            nextLevel = []

        return result