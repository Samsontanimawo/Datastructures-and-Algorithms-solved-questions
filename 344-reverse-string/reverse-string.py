class Solution(object):
    def reverseString(self, s):
               # Initialize two pointers, left and right, pointing to the start and end of the string
        left = 0
        right = len(s) - 1

        # Continue swapping characters from the outer ends towards the center
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]

            # Move the pointers towards the center
            left += 1
            right -= 1

        # Return the length of the reversed string (not the reversed string itself)
        return len(s)
        