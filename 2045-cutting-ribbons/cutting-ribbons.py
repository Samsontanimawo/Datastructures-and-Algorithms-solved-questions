class Solution(object):
    def maxLength(self, ribbons, k):
        
        left, right = 1, max(ribbons)
        
        while left <= right:
            mid = (left + right)//2
            result = 0
            
            for ribbon in ribbons:
                result += ribbon // mid
                
                
            if result >= k:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return right