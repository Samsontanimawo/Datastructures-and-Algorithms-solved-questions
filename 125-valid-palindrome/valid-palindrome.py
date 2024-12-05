class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left +=1

            while left < right and not s[right].isalnum():
                right -=1

            if s[left].lower() != s[right].lower():
                return False

            else:
                left +=1
                right -=1

        return True

# O(N) TIME
#O(1) SPACE