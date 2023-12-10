# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []

        hashmap, queue, minColumn, maxColumn = defaultdict(list), deque([(root, 0)]), 0, 0

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