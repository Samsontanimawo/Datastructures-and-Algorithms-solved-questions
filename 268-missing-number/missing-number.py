class Solution:
    def missingNumber(self, nums):
        # Initialize missingNumber with the length of the array,
        # assuming that the missing number is initially at the end of the range.
        missingNumber = len(nums)
        
        # Iterate through the array using both index and value.
        for index, num in enumerate(nums):
            # Update missingNumber by subtracting the current element value and
            # adding the current index, essentially comparing it with the expected sum.
            missingNumber += index - num
            
        # After the loop, missingNumber will hold the actual missing number.
        return missingNumber
