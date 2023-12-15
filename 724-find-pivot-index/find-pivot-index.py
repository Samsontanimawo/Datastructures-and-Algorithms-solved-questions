class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for index in range(len(nums)):
            total_sum -= nums[index]

            if left_sum == total_sum:
                return index

            left_sum += nums[index]

        return -1