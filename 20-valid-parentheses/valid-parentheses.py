class Solution:
    def isValid(self, s):
        # Dictionary to store the mappings of open and close brackets
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []

        # Iterate through the string
        for char in s:
            # If the character is an open bracket, push it to the stack
            if char in brackets:
                stack.append(char)
            # If the character is a close bracket
            elif char in brackets.values():
            # If the stack is empty or the top of the stack is not a corresponding open bracket, return False
                if not stack or brackets[stack.pop()] != char:
                    return False

        # Return True if the stack is empty, False otherwise
        return not stack