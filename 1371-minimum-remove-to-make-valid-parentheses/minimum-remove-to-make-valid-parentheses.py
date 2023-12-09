class Solution(object):
    def minRemoveToMakeValid(self, s):
        # Convert the input string to a list for easier modification
        convertStringToList = list(s)
        # Initialize a stack to keep track of indices of open parentheses
        stack = []

        # Iterate through the characters of the string
        for index in range(len(s)):
            # If an open parenthesis is encountered, push its index onto the stack
            if convertStringToList[index] == "(":
                stack.append(index)

            # If a closing parenthesis is encountered
            elif convertStringToList[index] == ")":
                # Check if there is a matching open parenthesis in the stack
                if stack:
                    stack.pop()  # Remove the matching open parenthesis index from the stack
                else:
                    # If no matching open parenthesis is found, replace the current closing parenthesis with an empty string
                    convertStringToList[index] = ""

        # Iterate through the remaining open parenthesis indices in the stack
        for index in stack:
            # Replace the open parenthesis at the index with an empty string
            convertStringToList[index] = ""

        # Join the modified list to obtain the final result
        return "".join(convertStringToList)