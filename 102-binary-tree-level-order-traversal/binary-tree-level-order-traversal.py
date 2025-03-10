class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [ root]
        level = []

        while queue:
            currentLevelValue = []

            for node in queue:
                currentLevelValue.append(node.val)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            result.append(currentLevelValue)

            queue = level
            level = []
        
        return result