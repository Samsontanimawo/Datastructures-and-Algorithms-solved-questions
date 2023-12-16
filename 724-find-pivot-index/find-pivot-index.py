class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums) # Sum of all the numbers = 1,7,3,6,5,6 = 28
        left_sum = 0

        for index in range(len(nums)):
            total_sum = total_sum - nums[index]

            if left_sum == total_sum:
                return index

            left_sum += nums[index]

        return -1