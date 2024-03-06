class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        left = 0
        zero_count = 0

        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count