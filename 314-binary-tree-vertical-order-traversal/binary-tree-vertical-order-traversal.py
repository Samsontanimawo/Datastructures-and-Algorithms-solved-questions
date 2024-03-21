class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return None

        minColumn = 0
        maxColumn = 0
        hashmap = defaultdict(list)
        queue = deque([(root, 0)])

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

# O(N) TIME AND SPACE