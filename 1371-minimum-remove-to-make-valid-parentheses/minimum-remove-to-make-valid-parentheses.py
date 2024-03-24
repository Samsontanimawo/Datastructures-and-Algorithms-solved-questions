class Solution(object):
    def minRemoveToMakeValid(self, s):
        # Initialize a variable to keep track of the balance of parentheses
        balance = 0
        
        # Convert the input string into a list of characters
        s = list(s)
        
        # First pass: Remove excess closing parentheses
        for index in range(len(s)):
            # If the current character is an opening parenthesis, increase the balance
            if s[index] == '(':
                balance += 1
            # If the current character is a closing parenthesis
            elif s[index] == ')':
                # If there are no corresponding opening parentheses for this closing one, remove it
                if balance == 0:
                    s[index] = ''
                # Otherwise, decrease the balance
                else:
                    balance -= 1
        
        # Second pass: Remove excess opening parentheses
        # Traverse the string backward
        for index in range(len(s) - 1, -1, -1):
            # If the balance is already restored to zero, exit the loop
            if balance == 0:
                break
            # If the current character is an opening parenthesis
            if s[index] == '(':
                # Remove it and decrement the balance
                s[index] = ''
                balance -= 1
        
        # Convert the modified list back into a string and return it
        return ''.join(s)

# Example usage:
solution = Solution()
print(solution.minRemoveToMakeValid("))(("))  # Output: ""
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
print(solution.minRemoveToMakeValid("a)b(c)d"))  # Output: "ab(c)d"
