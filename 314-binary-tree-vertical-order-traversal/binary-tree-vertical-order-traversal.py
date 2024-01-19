class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []

    # Initialize a hashmap to store nodes at each columnIndex
        hashmap = defaultdict(list)
    # Initialize a deque for level-order traversal with initial root and columnIndex 0
        queue = deque([(root, 0)])

    # Initialize min and max columns to keep track of the range of columns
        minColumn, maxColumn = 0, 0

    # Perform level-order traversal
        while queue:
            node, columnIndex = queue.popleft()
        # Append the node value to the corresponding columnIndex in the hashmap
            hashmap[columnIndex].append(node.val)

        # Update min and max columns
            minColumn = min(minColumn, columnIndex)
            maxColumn = max(maxColumn, columnIndex)

        # Enqueue left and right children with updated column indices
            if node.left:
                queue.append((node.left, columnIndex - 1))
            if node.right:
                queue.append((node.right, columnIndex + 1))

    # Generate the final output by iterating through the columns range
        return [hashmap[index] for index in range(minColumn, maxColumn + 1)]