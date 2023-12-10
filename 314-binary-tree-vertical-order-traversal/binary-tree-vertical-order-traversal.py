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


        minColumn = maxColumn = 0
        hashmap = defaultdict(list)
        queue = deque([(root, 0)]) # ROOT = NODE. 0 = COLUMN INDEX
 
        
        while queue:
            node, columnIndex = queue.popleft() # Pop off while there's something in the queue

            if node:
                hashmap[columnIndex].append(node.val)
                minColumn = min(minColumn, columnIndex)
                maxColumn = max(maxColumn, columnIndex)

            if node.left:
                queue.append((node.left, columnIndex -1))
                
            if node.right:
                queue.append((node.right, columnIndex + 1))

        return [hashmap[index] for index in range(minColumn, maxColumn + 1)]



