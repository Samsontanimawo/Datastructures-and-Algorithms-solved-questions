class Solution(object):
    def maximumCount(self, nums):
    # Initialize counter for negative numbers
        negative = 0

        # Iterate through the list to count negative numbers
        for num in nums:
            if num < 0:
                negative += 1
            else:
                break  # Stop counting once a non-negative number is encountered
        
        # Initialize counter for positive numbers
        positive = 0

        # Iterate through the list in reverse to count positive numbers
        for num in nums[:: -1]:
            if num > 0:
                positive += 1
            else:
                break  # Stop counting once a non-positive number is encountered
        
        # Return the maximum count between positive and negative numbers
        return max(positive, negative)