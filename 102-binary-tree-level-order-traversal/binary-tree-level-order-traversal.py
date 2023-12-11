
class Solution:
    def levelOrder(self, root):
        
        
        if not root:
            return None
        
        queue = [root]
        new_queue = []
        level = []
        result = []
        
        while queue:
            
            for root in queue:
                level.append(root.val)
                
                if root.left:
                    new_queue.append(root.left)
                    
                if root.right:
                    new_queue.append(root.right)
                    
            result.append(level)
            
            level = []
            queue = new_queue
            new_queue = []
            
        return result
    
    # O(N) TIME AND SPACE
        