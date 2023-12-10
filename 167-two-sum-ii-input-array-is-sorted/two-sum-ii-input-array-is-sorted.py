class Solution(object):
    def twoSum(self, nums, target):
        # Initialize two pointers, 'left' and 'right', at the beginning and end of the array.
        left = 0
        right = len(nums) - 1

        # Continue the loop until the 'left' pointer is less than the 'right' pointer.
        while left < right:
            # Calculate the sum of the elements at the 'left' and 'right' pointers.
            sum = nums[left] + nums[right]

            # Check if the sum is equal to the target.
            if sum == target:
                # If true, return the indices of the two numbers that add up to the target.
                # Note: The problem assumes that there is exactly one solution, so we return indices starting from 1.
                return [left + 1, right + 1]

            # If the sum is less than the target, move the 'left' pointer to the right.
            elif sum < target:
                left += 1

            # If the sum is greater than the target, move the 'right' pointer to the left.
            else:
                right -= 1
