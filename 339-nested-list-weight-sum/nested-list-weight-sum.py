class Solution(object):
    def depthSum(self, nestedList):
        
        def helper(list, depth):
            sum = 0
            
            for item in list:
                if item.isInteger():
                    sum += item.getInteger() * depth
                    
                else:
                    sum += helper(item.getList(), depth + 1)
                    
            return sum
        
        return helper(nestedList, 1)
    
"""
O(N) TIME
O(1) SPACE
"""