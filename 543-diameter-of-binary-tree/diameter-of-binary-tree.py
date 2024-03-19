class Solution:
    def diameterOfBinaryTree(self, root):
        # Initialize diameter variable to store the diameter of the binary tree
        self.diameter = 0
        
        # Define a function to calculate the height of a node in the binary tree
        def height(node):
            # Base case: If the node is empty, return 0
            if not node:
                return 0
            
            # Recursively calculate the height of the left and right subtrees
            else:
                left_height = height(node.left)
                right_height = height(node.right)
            
            # Update the diameter if the sum of left and right heights is greater
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        # Call the height function with the root node to start the process
        height(root)
        
        # Return the calculated diameter of the binary tree
        return self.diameter