class Solution:
    def removeDuplicates(self, s, k):
        stack = []  # Create an empty stack to store characters and their counts
        
        # Iterate through each character in the string
        for char in s:

            # If the stack is not empty and the current character is equal to the top character of the stack
            if stack and stack[-1][0] == char:

                # Increment the count of the top character
                stack[-1][1] += 1
                
                # If the count becomes equal to k, remove the top character from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # If the current character is different from the top character of the stack,
                # append it to the stack with a count of 1
                stack.append([char, 1])
        
        # Construct the final string from the characters remaining in the stack
        result = ''
        for char, count in stack:
            result += char * count
        
        return result