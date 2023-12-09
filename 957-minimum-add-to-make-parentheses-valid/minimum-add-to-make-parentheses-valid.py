#         (    (  )
#         0     1 2


class Solution(object):
    def minAddToMakeValid(self, s):
        addedP = closedP = openP = 0

        for index in range(len(s)):
            if s[index] == "(":
                openP +=1

            elif s[index] == ")":
                if openP > closedP:
                    closedP +=1

                else:
                    addedP +=1

        addedP += openP - closedP

        return addedP
        