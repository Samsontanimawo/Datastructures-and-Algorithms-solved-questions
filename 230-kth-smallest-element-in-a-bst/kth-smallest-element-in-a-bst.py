class Solution:
    def kthSmallest(self, root, k):
        
        def inorder(root):
            if not root:
                return []
            
            else:
                return inorder(root.left) + [root.val] + inorder(root.right) 
            
        return inorder(root)[k - 1]
    
    
    
 # root = [3,1,4,null,2, 7, 8, 9], k = 4

 # k-1 = answer = [1, 2, 3, 4, 7, 8, 9] - Sort the arrays using inorder travelsal [ left, root, right]
 # 4-1 = 3
 # The number in index 3 is kth 4th largest number      