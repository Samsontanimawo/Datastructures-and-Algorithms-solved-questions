class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0

        max_level = 1  # Initialize the level with the maximum sum to 1
        max_sum = float('-inf')  # Initialize the maximum sum to negative infinity

        queue = deque([(root, 1)])  # Use a deque to perform level order traversal

        while queue:
            level_size = len(queue)
            current_sum = 0

            for _ in range(level_size):
                node, level = queue.popleft()
                current_sum += node.val

                if node.left:
                   queue.append((node.left, level + 1))

                if node.right:
                    queue.append((node.right, level + 1))

        # Update the maximum sum and corresponding level
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level

        return max_level
