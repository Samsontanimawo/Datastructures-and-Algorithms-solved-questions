class Solution(object):
    def moveZeroes(self, nums):
        left = right = 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1

            right +=1

        return len(nums)