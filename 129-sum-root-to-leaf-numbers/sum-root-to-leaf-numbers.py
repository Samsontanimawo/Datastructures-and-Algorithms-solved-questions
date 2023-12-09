class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        
        def helper(node, sum):
            if not node:
                return 0
            
            sum = sum * 10 + int(node.val)
            
            if not node.left and not node.right:
                return sum
            
            else:
                return helper(node.left, sum) + helper(node.right, sum)
            
        return helper(root, 0)
        