class Solution(object):
    def minAddToMakeValid(self, s):
        addedP = closedP = openP = 0

        for char in s:
            if char == "(":
                openP +=1

            elif char == ")":
                if closedP < openP:
                    closedP +=1

                else:
                    addedP +=1

        addedP += openP - closedP

        return addedP

# O(N) time | O(1) SPACE
        