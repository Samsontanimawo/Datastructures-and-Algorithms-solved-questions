class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Perform cyclic sort to place each number at its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the smallest positive integer that is not present
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


