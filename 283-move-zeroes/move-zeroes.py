class Solution:
    def moveZeroes(self, nums):
        
        # nums = [0,1,0,3,12]
        # Output: [1,3,12,0,0]

        left = 0
        N = len(nums)

        for right in range(N):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1