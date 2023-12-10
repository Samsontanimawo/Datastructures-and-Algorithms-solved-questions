class Solution(object):
    def verticalOrder(self, root):

        if not root:
            return []

        minColumn, maxColumn, queue, hashmap = 0, 0, deque([(root, 0)]), defaultdict(list)

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