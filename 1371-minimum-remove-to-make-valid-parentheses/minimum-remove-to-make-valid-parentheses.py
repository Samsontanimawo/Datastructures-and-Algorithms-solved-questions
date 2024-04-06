class Solution(object):
    def minRemoveToMakeValid(self, s):
        s = list(s)
        n = len(s)
        stack = []

        for index in range(n):
            if s[index] == "(":
                stack.append(index)

            elif s[index] == ")":
                if stack:
                    stack.pop()

                else:
                    s[index] = ""

        for index in stack:
            s[index] = ""
            
        return "".join(s)