class Solution:
    def missingNumber(self, nums):
        
        missingNumber = len(nums)
        
        for index, num in enumerate(nums):
            missingNumber += index - num
            
        return missingNumber