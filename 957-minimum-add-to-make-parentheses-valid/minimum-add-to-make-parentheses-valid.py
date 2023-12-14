class Solution(object):
    def minAddToMakeValid(self, s):
        openP = closedP = addedP = 0

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

        # O(N) Time | O(1) SPACE