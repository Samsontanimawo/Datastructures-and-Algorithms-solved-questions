class Solution(object):
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1

        return len(nums)

# O(N) Time and O(1) SPACE