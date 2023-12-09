class Solution(object):
    def minRemoveToMakeValid(self, s):
        convertStringToList = list(s)
        stack = []

        for index in range(len(s)):
            if convertStringToList[index] == "(":
                stack.append(index)

            elif s[index] == ")":
                if stack:
                    stack.pop()

                else:
                    convertStringToList[index] = ""

        for index in stack:
            convertStringToList[index] = ""

        return "".join(convertStringToList)