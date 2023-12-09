class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Base case: if the root is None, return None
        if not root:
            return None

        # If the root is either p or q, it is a common ancestor
        elif root == p or root == q:
            return root

        else:
            # Recursively find the common ancestor in the left subtree
            left = self.lowestCommonAncestor(root.left, p, q)
            # Recursively find the common ancestor in the right subtree
            right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees have common ancestors, return the root
        if left and right:
            return root

        # If only one subtree has a common ancestor, return that ancestor
        else:
            return left or right

# Call the lowestCommonAncestor function with a binary tree root and nodes p, q


# Print the result
# print(Solution().lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4])
