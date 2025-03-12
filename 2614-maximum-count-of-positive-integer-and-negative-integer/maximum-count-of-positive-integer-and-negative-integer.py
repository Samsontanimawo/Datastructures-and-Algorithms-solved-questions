class Solution(object):
    def maximumCount(self, nums):
    # Count negative numbers
        neg = 0
        for num in nums:
            if num < 0:
                neg += 1
            else:
                break
        
        # Count positive numbers
        pos = 0
        for num in reversed(nums):
            if num > 0:
                pos += 1
            else:
                break
        
        return max(pos, neg)

