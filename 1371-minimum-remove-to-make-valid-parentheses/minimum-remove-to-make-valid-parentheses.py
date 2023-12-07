# ()))
# "lee(t(c)o)de)"
# [   (     ]

class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack, s, N = [], list(s), len(s)

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