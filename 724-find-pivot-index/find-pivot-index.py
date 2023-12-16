class Solution(object):
    def pivotIndex(self, nums):
        right_sum = sum(nums) # Sum of all the numbers = 1,7,3,6,5,6 = 28
        left_sum = 0

        for index in range(len(nums)):
            right_sum = right_sum - nums[index] # numbers index = currentNumber. E.g 1

            if left_sum == right_sum:
                return index

            else:
                left_sum = left_sum + nums[index] # numbers index = currentNumber. E.g 1

        return -1