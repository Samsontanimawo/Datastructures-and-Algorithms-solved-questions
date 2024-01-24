class Solution(object):
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []        

        for char in range(len(s)):
            if s[char] == "(":
                stack.append(char)

            elif s[char] == ")":
                if stack:
                    stack.pop()

                else:
                    s[char] = ""

        for char in stack:
            s[char] = ""

        return "".join(s)