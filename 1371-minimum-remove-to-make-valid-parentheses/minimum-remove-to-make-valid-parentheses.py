class Solution(object):
    def minRemoveToMakeValid(self, s):
        s, N, stack = list(s), len(s), []

        for index in range(N):
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