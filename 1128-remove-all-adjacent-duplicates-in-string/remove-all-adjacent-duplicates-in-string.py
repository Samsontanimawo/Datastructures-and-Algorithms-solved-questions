class Solution(object):
    def removeDuplicates(self, s):
        stack = []  # Initialize an empty stack to keep track of characters

    # Iterate through each character in the input string
        for char in s:
        # Check if the stack is not empty and the current character matches the top of the stack
            if stack and stack[-1] == char:
                stack.pop()  # If there's a match, remove the character from the stack
            else:
                stack.append(char)  # If no match, push the current character onto the stack

        return ''.join(stack)  # Convert the stack to a string and return the final result

        