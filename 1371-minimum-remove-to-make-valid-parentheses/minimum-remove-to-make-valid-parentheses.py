class Solution(object):
    def minRemoveToMakeValid(self, s):
        open_count = 0
        to_remove_left = set()
        to_remove_right = set()

    # First pass: Mark invalid left parentheses
        for i, char in enumerate(s):
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    to_remove_right.add(i)

    # Second pass: Mark invalid right parentheses
        open_count = 0
        for i in range(len(s) - 1, -1, -1):
           char = s[i]
           if char == ')':
               open_count += 1
               
           elif char == '(':
               if open_count > 0:
                   open_count -= 1
               else:
                   to_remove_left.add(i)

    # Combine all indices to remove
        to_remove = to_remove_left.union(to_remove_right)

        result = []
        for i, char in enumerate(s):
           if i not in to_remove:
               result.append(char)

        return ''.join(result)