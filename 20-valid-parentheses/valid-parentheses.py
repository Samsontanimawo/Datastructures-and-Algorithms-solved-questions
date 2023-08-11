class Solution(object):
    def isValid(self, s):
        
        stack = []
        mappedBrackets = { ']':'[', ')':'(', '}':'{'}

        for char in s:
            if char in mappedBrackets:
                if stack and stack[-1] == mappedBrackets[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)

        return stack == []