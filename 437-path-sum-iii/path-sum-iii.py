class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, running_sum):
            if not node:
                return 0
            
            # Count paths starting from the current node
            paths_from_current = 1 if node.val == running_sum else 0
            
            # Update running sum for the child nodes
            running_sum -= node.val
            
            # Count paths from the left and right subtrees
            paths_from_left = dfs(node.left, running_sum)
            paths_from_right = dfs(node.right, running_sum)
            
            # Total paths from the current node
            total_paths = paths_from_current + paths_from_left + paths_from_right
            
            return total_paths
        
        if not root:
            return 0
        
        # Start DFS traversal from the root
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

# Example usage:
# Construct the binary tree
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(-3)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(2)
root1.right.right = TreeNode(11)
root1.left.left.left = TreeNode(3)
root1.left.left.right = TreeNode(-2)
root1.left.right.right = TreeNode(1)

target_sum1 = 8
print(Solution().pathSum(root1, target_sum1))  # Output: 3

root2 = TreeNode(5)
root2.left = TreeNode(4)
root2.right = TreeNode(8)
root2.left.left = TreeNode(11)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(4)
root2.left.left.left = TreeNode(7)
root2.left.left.right = TreeNode(2)
root2.right.right.left = TreeNode(5)
root2.right.right.right = TreeNode(1)

target_sum2 = 22
print(Solution().pathSum(root2, target_sum2))  # Output: 3
