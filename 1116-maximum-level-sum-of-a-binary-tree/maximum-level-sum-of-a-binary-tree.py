from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        # Check if the tree is empty
        if not root:
            return 0

        max_level = 1  # Initialize the level with the maximum sum to 1
        max_sum = float('-inf')  # Initialize the maximum sum to negative infinity
        level = 1 # To keep track of the current level
        queue = [root] # Put the first number of the tree in the queue

        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            else:
                queue = next_level
                level +=1

        return max_level





        