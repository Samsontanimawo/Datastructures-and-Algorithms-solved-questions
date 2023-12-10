class Solution:
    def twoSum(self, nums, target):
    # Create a dictionary to store the indices of elements
        num_indices = {}

        for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_indices:
            # Return the indices of the two numbers
                return [num_indices[complement], i]

        # Store the current number and its index in the dictionary
            num_indices[num] = i

    # If no solution is found
        return None

# Example usage:
#nums = [2, 7, 11, 15]
#target = 9
#result = twoSum(nums, target)
#print(result)  # Should print [0, 1]
