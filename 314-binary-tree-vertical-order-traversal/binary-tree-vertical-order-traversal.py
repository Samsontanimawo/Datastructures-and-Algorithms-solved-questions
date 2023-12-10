from collections import deque, defaultdict

class Solution(object):
    def verticalOrder(self, root):
        # Base case: If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize variables: minColumn and maxColumn for column range,
        # queue for BFS, and hashmap to store nodes at each column
        minColumn, maxColumn, queue, hashmap = 0, 0, deque([(root, 0)]), defaultdict(list)

        # Perform BFS traversal
        while queue:
            node, column = queue.popleft()

            # Check if the node is not None
            if node:
                # Store the node's value in the hashmap at the corresponding column
                hashmap[column].append(node.val)

                # Update minColumn and maxColumn based on the current column
                minColumn = min(minColumn, column)
                maxColumn = max(maxColumn, column)

                # Enqueue the left child with a decreased column index
                queue.append((node.left, column - 1))
                # Enqueue the right child with an increased column index
                queue.append((node.right, column + 1))

        # Construct the result by extracting nodes' values for each column
        result = [hashmap[index] for index in range(minColumn, maxColumn + 1)]

        return result

"""
O(N) TIME & SPACE
"""
