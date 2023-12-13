class Solution(object):
    def missingElement(self, nums, k):
        # Initialize left and right pointers for binary search
        left = 0
        right = len(nums) - 1

        # Perform binary search until left and right pointers meet
        while left < right:
            # Calculate the middle index
            mid = (left + right + 1) // 2

            # Check if the number of missing elements up to mid is less than k
            if nums[mid] - nums[0] - mid < k:
                left = mid  # If true, update the left pointer

            else:
                right = mid - 1  # If false, update the right pointer

        # The result is the sum of the first element, k, and the left pointer
        return nums[0] + k + left
