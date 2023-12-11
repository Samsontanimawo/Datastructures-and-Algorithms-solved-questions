class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return None

        minColumn = maxColumn = 0 # Both column starts at [00]
        hashmap = defaultdict(list) # The key = column. The value is the list value for every node in the column
        queue = deque([(root, 0)]) # Use breath first search = It uses queue. Depth first search uses stack

        while queue:
            node, columnIndex = queue.popleft()

            if node:
                hashmap[columnIndex].append(node.val)
                minColumn = min(minColumn, columnIndex)
                maxColumn = max(maxColumn, columnIndex)

            if node.left:
                queue.append((node.left, columnIndex - 1))

            if node.right:
                queue.append((node.right, columnIndex + 1))

        return [hashmap[index] for index in range(minColumn, maxColumn + 1)]
        # +1 because ranges are not inclusive at the endpoint. We need to use the last endpoint.

            

        
        