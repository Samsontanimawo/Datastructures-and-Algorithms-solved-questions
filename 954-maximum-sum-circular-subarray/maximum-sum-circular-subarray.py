class Solution:
    def maxSubarraySumCircular(self, nums):
        max_sum_without_wrap = self.maxSubArraySum(nums)
        
        total_sum = sum(nums)
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        min_sum_without_wrap = self.maxSubArraySum(nums)
        
        max_sum_with_wrap = total_sum + min_sum_without_wrap
        
        if max_sum_with_wrap == 0:
            return max_sum_without_wrap
        
        return max(max_sum_without_wrap, max_sum_with_wrap)
    
    def maxSubArraySum(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

# Test cases
solution = Solution()
nums1 = [1, -2, 3, -2]
nums2 = [5, -3, 5]
nums3 = [3, -1, 2, -1]

print(solution.maxSubarraySumCircular(nums1))  # Output: 3
print(solution.maxSubarraySumCircular(nums2))  # Output: 10
print(solution.maxSubarraySumCircular(nums3))  # Output: 4
