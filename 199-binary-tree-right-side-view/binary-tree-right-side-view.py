# DATA STRUCTURES
# ALGORITHMS
# TIME AND SPACE COMPLEXITY
# Standing on the right side of a tree
# Return the values I can see
# Ignore the values I can't see.
# If i'm on the right side, I can't see any left side value
# What algorithm should I use?
# Keep track of the root. If there's no root, what should I return?
# We can traverse a tree in DFS or BFS. Which one should I use?
# Since we don't care about the left side values, let's use BFS
# If we're using BFS, then let's use QUEUE.
# Put the first value in the queue
# Keep track of the levels and reset it
# Put pop the nodes in the queue and add them to result list
# Return the list

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        queue = [root]
        level = []
        result = []

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

        # O(N) TIME AND SPACE


        