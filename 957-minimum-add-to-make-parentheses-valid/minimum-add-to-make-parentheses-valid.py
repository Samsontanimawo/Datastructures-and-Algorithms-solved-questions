# ((()

class Solution(object):
    def minAddToMakeValid(self, s):
        openP = closedP = addedP = 0

        for index in range(len(s)):
            if s[index] == "(":
                openP +=1

            elif s[index] == ")":
                if closedP < openP:
                    closedP +=1
                else:
                    addedP +=1

        addedP += openP - closedP

        return addedP

                