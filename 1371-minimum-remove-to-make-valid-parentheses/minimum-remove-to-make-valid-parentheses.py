class Solution(object):
    def minRemoveToMakeValid(self, string):
        stack = []
        string = list(string)

        for index in range(len(string)):
            if string[index] == "(":
                stack.append(index)

            elif string[index] == ")":
                if stack:
                    stack.pop()

                else:
                    string[index] = ""

        for index in stack:
            string[index] = ""

        
        return "".join(string)
        