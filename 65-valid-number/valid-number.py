import re

class Solution:
    def isNumber(self, s):
        # Define the regular expression pattern for a valid number
        pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')

        # Use the pattern to match the input string
        match = pattern.match(s)

        # Check if the entire string matches the pattern
        return match is not None

# Example usage:
#solution = Solution()
#print(solution.isNumber("0"))  # Output: True
