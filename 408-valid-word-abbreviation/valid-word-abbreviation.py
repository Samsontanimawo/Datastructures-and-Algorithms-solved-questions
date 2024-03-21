# Input: word = "internationalization", abbr = "i12iz4n"
#                L                              R

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        left = 0
        right = 0

        while left < len(word) and right < len(abbr):
            if word[left] == abbr[right]:
                left +=1
                right +=1
            
            else:
                if not abbr[right].isdigit() or abbr[right] == "0":
                    return False

                else:
                    steps = 0

                while right < len(abbr) and abbr[right].isdigit():
                    steps = steps * 10 + int(abbr[right])
                    right +=1

                left += steps    

        return left == len(word) and right == len(abbr)
        # O(M x N) TIME
        # O(1) SPACE