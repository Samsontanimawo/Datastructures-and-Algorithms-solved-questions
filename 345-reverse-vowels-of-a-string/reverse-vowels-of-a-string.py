class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s)-1
        vowels = set("aAeEiIoOuU")

        while left < right:
            while left < right and not s[left] in vowels:
                left +=1

            while left < right and not s[right] in vowels:
                right -=1

            s[left] , s[right] = s[right], s[left]
            left +=1
            right -=1
               
        return "".join(s)