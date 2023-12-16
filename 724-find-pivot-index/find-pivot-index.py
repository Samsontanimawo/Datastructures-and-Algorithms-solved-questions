class Solution(object):
    def pivotIndex(self, nums):
        totalSum = sum(nums)

        leftSum = 0

        for index in range(len(nums)):
            totalSum = totalSum - nums[index]

            if leftSum == totalSum:
                return index

            else:
                totalSum -= nums[index]

        return -1