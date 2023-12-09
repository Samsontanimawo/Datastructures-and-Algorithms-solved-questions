class Solution(object):
    def validPalindrome(self, s):

        # Helper function to check if a substring is a palindrome
        def palindromeCheck(left, right):
            while left < right:
                # If characters don't match, it's not a palindrome
                if s[left] != s[right]:
                    return False
                else:
                    # Move pointers towards the center
                    left += 1
                    right -= 1

            # If the loop completes, the substring is a palindrome
            return True

        # Initialize pointers at the beginning and end of the string
        left, right = 0, len(s) - 1

        # Iterate through the string from both ends towards the center
        while left < right:
            
            # If characters don't match
            if s[left] != s[right]:
                # Check if making either of the characters equal will result in a palindrome
                return palindromeCheck(left + 1, right) or palindromeCheck(left, right - 1)
            else:
                # Move pointers towards the center
                left += 1
                right -= 1

        # If the loop completes, the string is a valid palindrome
        return True

# print(Solution().validPalindrome("ABAHDDDDADFA"))