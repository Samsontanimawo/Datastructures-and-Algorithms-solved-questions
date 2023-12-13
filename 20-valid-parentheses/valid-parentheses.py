class Solution(object):
    def isValid(self, s):
        openP = "({["
        closedP = ")}]"

        stack = []

        for char in s:
            if char in openP:
                stack.append(char)

            elif char in closedP:
                if not stack or openP.index(stack.pop()) != closedP.index(char):
                    return False

            else:
                return False

        return stack == []
