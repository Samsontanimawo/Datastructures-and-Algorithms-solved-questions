class Solution(object):
    def removeVowels(self, s):
        vowels = " aAeEiIoOuU"
        result = []

        for char in s:
            if char not in vowels:
                result.append(char)

        return "".join(result)

        