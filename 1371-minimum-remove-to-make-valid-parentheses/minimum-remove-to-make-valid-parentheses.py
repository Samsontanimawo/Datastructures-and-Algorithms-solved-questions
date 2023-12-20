#Input: s = "lee(t(c)o)de)"
# Input: s = "l   e   e   (   t  (  c  )  o  ) d   e   )"
#             0   1   2   3  4   5  6  7  8  9 10  11  12
# STACK = [l e   e   t c o  d   e )]
# New stack = l   e   e   (   t  (  c  )  o  ) d   e
# Convert the list to s = lee(t(c)o)de
# Output = "lee(t(c)o)de"

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

           #else:
               # stack.append(index)

       for index in stack:
            s[index] = ""

       return "".join(s)