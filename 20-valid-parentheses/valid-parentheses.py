class Solution(object):
    def isValid(self, s):
        brackets = { ")":"(", "]":"[","}":"{" }
        stack = []
        
        for char in s:
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return stack == []

            