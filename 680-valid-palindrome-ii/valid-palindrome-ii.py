class Solution(object):
    def validPalindrome(self, s):
        def palindromeCheck(left, right):
            
            while left < right:
                if s[left] != s[right]:
                    return False

                else:
                    left +=1
                    right -=1

            return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return palindromeCheck(left + 1, right) or palindromeCheck(left, right - 1)

            else:
                left +=1
                right -=1

        return True

    