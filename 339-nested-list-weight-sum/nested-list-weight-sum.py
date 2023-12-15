class Solution(object):
    def depthSum(self, nestedList):
        
        def helper(list, level):
            sum = 0
            
            for item in list:
                if item.isInteger():
                    sum += item.getInteger() * level
                    
                else:
                    sum += helper(item.getList(), level + 1)
                    
            return sum
        
        return helper(nestedList, 1)
    
"""
O(N) TIME
O(1) SPACE
"""