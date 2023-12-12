class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        # word = "internationalization", abbr = "i12iz4n"
        #         LEFT                    RIGHT
        
        left = right = 0

        while left < len(word) and right < len(abbr):
            if word[left] != abbr[right]:
                if not abbr[right].isdigit():
                    return False

                else:
                    if abbr[right] == "0":
                        return False

                    steps = 0

                    while right < len(abbr) and abbr[right].isdigit():
                        steps = steps * 10 + int(abbr[right])
                        right +=1

                    left += steps

            else:
                left +=1
                right +=1

        return left == len(word) and right == len(abbr)
