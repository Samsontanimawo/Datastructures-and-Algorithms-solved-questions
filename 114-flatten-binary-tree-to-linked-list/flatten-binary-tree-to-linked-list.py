class Solution:
    def flatten(self, root):
        # Base case: if the root is None or a leaf node, no modification needed
        if not root or (not root.left and not root.right):
            return
        
        # Flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Save the right subtree
        right_subtree = root.right
        
        # Make the left subtree the new right subtree
        root.right = root.left
        root.left = None
        
        # Find the end of the new right subtree and attach the saved right subtree
        while root.right:
            root = root.right
        root.right = right_subtree