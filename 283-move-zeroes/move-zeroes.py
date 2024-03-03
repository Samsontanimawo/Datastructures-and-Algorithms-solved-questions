class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        right = 0

        # Iterate through the array using a while loop
        while right < len(nums):
            # If a non-zero element is found, swap it with the left pointer
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # Move the left pointer to the right
            right += 1  # Move the right pointer to the right

        return len(nums)
