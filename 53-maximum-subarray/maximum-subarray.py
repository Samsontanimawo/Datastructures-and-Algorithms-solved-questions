class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]  # Initialize max_sum with the first element
        current_sum = nums[0]  # Initialize current_sum with the first element

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update current_sum by adding the current number or starting a new subarray
            current_sum = max(num, current_sum + num)
            # Update max_sum to track the maximum sum seen so far
            max_sum = max(max_sum, current_sum)

        return max_sum

# Test cases
solution = Solution()
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]

print(solution.maxSubArray(nums1))  # Output: 6
print(solution.maxSubArray(nums2))  # Output: 1
print(solution.maxSubArray(nums3))  # Output: 23
