class Solution(object):
    def isPalindrome(self, s):
        # Initialize two pointers, 'left' at the beginning and 'right' at the end of the string
        left, right = 0, len(s) - 1

        # Continue the loop as long as 'left' pointer is less than 'right' pointer
        while left < right:
            # Move 'left' pointer to the right until a valid alphanumeric character is found
            while left < right and not s[left].isalnum():
                left += 1

            # Move 'right' pointer to the left until a valid alphanumeric character is found
            while left < right and not s[right].isalnum():
                right -= 1

            # Check if the characters at 'left' and 'right' positions are not equal (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False  # If not equal, it's not a palindrome

            else:
                # Move both pointers inward as the characters are equal
                left += 1
                right -= 1

        # If the loop completes without returning False, the string is a palindrome
        return True
