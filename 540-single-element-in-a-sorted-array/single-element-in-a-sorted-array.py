class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (right + left) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return nums[left]  # or nums[right]

# Test cases
nums1 = [1,1,2,3,3,4,4,8,8]
nums2 = [3,3,7,7,10,11,11]

solution = Solution()
print(solution.singleNonDuplicate(nums1))  # Output: 2
print(solution.singleNonDuplicate(nums2))  # Output: 10
