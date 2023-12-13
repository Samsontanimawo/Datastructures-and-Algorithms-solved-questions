class Solution(object):
    def singleNonDuplicate(self, nums):
    # Initialize the result to 0. Since XOR with 0 does not change a number,
# this will be the neutral element for XOR.
        result = 0

# Loop through each number in the array.
        for num in nums:
    # Use XOR operation to update the result.
    # XORing a number with itself results in 0,
    # and XORing 0 with a number doesn't change the number.
            result = num ^ result

# After the loop, 'result' will contain the XOR of all elements in the array.
# The unique element that appears only once will be the final value of 'result'.

# Return the unique element.
        return result
