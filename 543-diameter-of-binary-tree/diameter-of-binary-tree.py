class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Check if the tree is empty
        if not root:
            return 0  # If the tree is empty, the diameter is 0

        # Calculate the height and diameter for the left and right subtrees
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)

        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        # Return the maximum of the three possibilities: leftHeight + rightHeight, leftDiameter, rightDiameter
        return max((leftHeight + rightHeight), max(leftDiameter, rightDiameter))
        
    def maxHeight(self, node):
        # Base case: return 0 if the node is empty
        if not node:
            return 0

        # Recursively calculate the height of the subtree
        return 1 + max(self.maxHeight(node.left), self.maxHeight(node.right))

# Example usage:
# Construct the tree: [1, 2, 3, 4, 5]
#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)

#solution = Solution()
#print(solution.diameterOfBinaryTree(root))  # Output: 3
