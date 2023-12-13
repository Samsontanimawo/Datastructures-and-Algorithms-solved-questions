class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

        # Make mid even to ensure we compare elements at even indices
            if mid % 2 == 1:
                mid -= 1

        # Check if the single element is on the left or right side
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


# nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
 #              L      
        