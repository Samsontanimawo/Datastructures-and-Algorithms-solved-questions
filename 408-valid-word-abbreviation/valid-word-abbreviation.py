

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        left, right = 0, 0
        while left < len(word) and right < len(abbr):
            if word[left] == abbr[right]:
                left += 1
                right += 1
            elif abbr[right].isdigit():
                if abbr[right] == '0':  # Check for leading zeros
                    return False
                steps = 0
                while right < len(abbr) and abbr[right].isdigit():
                    steps = steps * 10 + int(abbr[right])
                    right += 1
                left += steps
            else:
                return False
        return left == len(word) and right == len(abbr)

# Test cases
solution = Solution()
print(solution.validWordAbbreviation("internationalization", "i12iz4n"))  # Output: True
print(solution.validWordAbbreviation("apple", "a2e"))  # Output: False
