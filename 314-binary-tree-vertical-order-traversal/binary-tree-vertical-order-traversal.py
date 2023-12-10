# Keep track of the min column value
# Keep track of the max column
# Use a default dictionary = defaultdict(list)
# When we go left of the tree = negative
# When we go right of the tree = positive
#[3,  9,  8,  4,  0,  1,  7,  2,  5]
# 0   -1  +1  -2  0   0   +2 +1  -1 -- Column index
# We need a queue for level order traversal. FIFO PRINCIPLE

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []

        # Initialize minColumn and maxColumn
        minColumn = maxColumn = 0
        # Use a defaultdict to store nodes at each column
        hashmap = defaultdict(list)
        # Use a deque for level order traversal (FIFO)
        queue = deque([(root, 0)])  # ROOT = NODE. 0 = COLUMN INDEX
 
        while queue:
            # Pop off while there's something in the queue
            node, columnIndex = queue.popleft()

            if node:
                # Store the node's value in the hashmap at the corresponding column
                hashmap[columnIndex].append(node.val)
                # Update minColumn and maxColumn based on the current column index
                minColumn = min(minColumn, columnIndex)
                maxColumn = max(maxColumn, columnIndex)

            if node.left:
                # Enqueue the left child with a decreased column index
                queue.append((node.left, columnIndex - 1))
                
            if node.right:
                # Enqueue the right child with an increased column index
                queue.append((node.right, columnIndex + 1))

        # Construct the result by extracting nodes' values for each column
        return [hashmap[index] for index in range(minColumn, maxColumn + 1)]
