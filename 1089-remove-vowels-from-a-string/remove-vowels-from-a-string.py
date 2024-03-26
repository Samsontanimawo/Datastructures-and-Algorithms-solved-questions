# Find the words that are not vowels

class Solution(object):
  def removeVowels(self, s):
    s = list(s)
    left = 0
    right = len(s)-1
    vowels = "aAeEiIoOuU"

    return "".join(char for char in s if char not in vowels)

