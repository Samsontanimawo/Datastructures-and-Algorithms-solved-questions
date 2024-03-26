# Find the words that are not vowels

class Solution(object):
  def removeVowels(self, s):
    s = list(s)
    vowels = "aAeEiIoOuU"

    return "".join(char for char in s if char not in vowels)