class Solution(object):
    def reverseWords(self, s):
        # Goal is to reverse words in a string
        # Hello Wolrd = World hello
        # How do we know a word is formed?
        # Can we use 2 pointers
        # The string may contain only 1 space
        # How can we use the space for our benefit?
        

        words = s.split()
        reversed_words = words[::-1]

        return " ".join(reversed_words)