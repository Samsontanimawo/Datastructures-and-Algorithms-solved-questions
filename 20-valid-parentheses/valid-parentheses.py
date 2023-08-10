class Solution(object):
    def isValid(self, s):
        
        stack = []
        mapBrackets = { ')':'(', '}':'{', ']':'[' }

        for char in s:
            if char in mapBrackets:
                if stack and stack[-1] == mapBrackets[char]:
                    stack.pop()
                    
                else:
                    return False

            else:
                stack.append(char)

        return stack == []