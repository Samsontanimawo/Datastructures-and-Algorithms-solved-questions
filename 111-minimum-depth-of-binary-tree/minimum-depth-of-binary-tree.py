class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        elif not root.left:
            return 1 + self.minDepth(root.right)
        
        elif not root.right:
            return 1 + self.minDepth(root.left)
        
        else:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))