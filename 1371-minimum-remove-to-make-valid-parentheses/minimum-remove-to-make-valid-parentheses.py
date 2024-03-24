class Solution(object):
    def minRemoveToMakeValid(self, s):
        balance = 0
        s = list(s)
        
        # First pass: Remove excess closing parentheses
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            elif s[i] == ')':
                if balance == 0:
                    s[i] = ''
                else:
                    balance -= 1
        
        # Second pass: Remove excess opening parentheses
        for i in range(len(s) - 1, -1, -1):
            if balance == 0:
                break
            if s[i] == '(':
                s[i] = ''
                balance -= 1
        
        return ''.join(s)

# Example usage:
solution = Solution()
print(solution.minRemoveToMakeValid("))(("))  # Output: ""
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
print(solution.minRemoveToMakeValid("a)b(c)d"))  # Output: "ab(c)d"
