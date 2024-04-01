class Solution:
    def lengthOfLastWord(self, s):
        # Initialize variables
        index, length = len(s), 0

        # Iterate through the string from right to left
        while index > 0:
            index -= 1  # Move the index one position to the left

            # If the character is not a space, it's part of the last word
            if s[index] != ' ':
                length += 1
            # If we encounter a space and we've already counted some characters (i.e., we're in the last word),
            # return the length of the last word
            elif length > 0:
                return length

        # Return the length of the last word
        return length
