class Solution(object):
    def missingElement(self, nums, k):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right + 1) // 2

            if nums[mid] - nums[0] - mid < k:
                left = mid

            else:
                right = mid - 1

        return nums[0] + k + left