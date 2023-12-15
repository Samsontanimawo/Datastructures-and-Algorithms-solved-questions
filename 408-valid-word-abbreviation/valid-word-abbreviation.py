class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        # Initialize pointers for the word and abbreviation
        left = right = 0

        # Iterate through the word and abbreviation
        while left < len(word) and right < len(abbr):
            # If characters don't match
            if word[left] != abbr[right]:
                # Check if the abbreviation character is not a digit or is '0'
                if not abbr[right].isdigit() or abbr[right] == "0":
                    return False

                # Extract the number of characters to skip
                steps = 0
                while right < len(abbr) and abbr[right].isdigit():
                    steps = steps * 10 + int(abbr[right])
                    right += 1

                # Skip the specified number of characters in the word
                left += steps

            else:
                # If characters match, move both pointers
                left += 1
                right += 1

        # Check if both pointers reached the end of their respective strings
        return left == len(word) and right == len(abbr)