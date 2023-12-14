class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        s = list(s)

        for char in s:
            if char in stack and stack[-1] == char:
                stack.pop()

            else:
                stack.append(char)

        return "".join(stack)
# O(N) Time and Space        