class Solution(object):
    def moveZeroes(self, nums):
        # Initialize the left pointer at the beginning of the array
        left = 0

        # Iterate through the array using the right pointer
        for right in range(len(nums)):
            # Check if the current element is not zero
            if nums[right] != 0:
                # Swap the non-zero element with the element at the left pointer
                nums[left], nums[right] = nums[right], nums[left]
                
                # Move the left pointer to the next position
                left += 1
                # Note: right does not increment in this case, as the element at the 'right' index has been swapped
                # We decrement right to re-check the current position after the swap

        # The length of the array is returned (though it is not required by the problem)
        return len(nums)
