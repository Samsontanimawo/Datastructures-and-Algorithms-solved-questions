class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        rightSideView = []
        queue = [root]

        while queue:
            nextLevel = []  # Initialize nextLevel for the current level

            for node in queue:
                if node.left:
                    nextLevel.append(node.left)

                if node.right:
                    nextLevel.append(node.right)

            # Append the value of the rightmost node at the current level
            rightSideView.append(node.val)
            queue = nextLevel
            nextLevel = []


        return rightSideView
