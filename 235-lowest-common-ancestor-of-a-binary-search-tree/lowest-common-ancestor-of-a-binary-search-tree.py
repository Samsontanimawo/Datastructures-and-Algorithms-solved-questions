class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        else:
            return left or right

        # O(N) Time and Space