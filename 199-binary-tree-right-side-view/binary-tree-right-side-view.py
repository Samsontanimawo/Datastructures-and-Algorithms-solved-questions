class Solution(object):
    def rightSideView(self, root):
        # Check if the root is None (empty tree), return an empty list if true
        if not root:
            return []

        result = []  # This will store the final right side view of the tree
        level = []  # This will temporarily hold the nodes for the next level
        queue = [root]  # Start with the root node in the queue

        # Traverse the tree level by level
        while queue:
            # For each level, go through all the nodes
            for node in queue:
                # If the node has a left child, add it to the next level's list
                if node.left:
                    level.append(node.left)

                # If the node has a right child, add it to the next level's list
                if node.right:
                    level.append(node.right)

            # Append the value of the last node in the current level (rightmost node)
            result.append(node.val)

            # Move to the next level by updating the queue with the new nodes
            queue = level
            level = []  # Clear the level list to prepare for the next level

        # Return the result which contains the right side view of the tree
        return result
