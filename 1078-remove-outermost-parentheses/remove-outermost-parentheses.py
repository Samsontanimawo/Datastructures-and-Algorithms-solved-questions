class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        balance = 0

        for char in s:
            if char == '(':
                if balance > 0:
                    result.append(char)
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    result.append(char)

        return ''.join(result)

# Example
# s = "(()())(())"
# output = removeOuterParentheses(s)
# print(output)  # Output: "()()()"

        