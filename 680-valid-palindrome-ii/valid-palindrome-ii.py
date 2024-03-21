class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s)-1

        def palindromeCheck(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                else:
                    left +=1
                    right -=1

            return True

   
        while left < right:
            if s[left] != s[right]:
                return palindromeCheck(left + 1, right) or palindromeCheck(left, right - 1)

            else:
                left +=1
                right -=1

        return True