class Solution(object):
    def isNumber(self, s):
        decimal = digit = exponent = symbol = False

        for char in s:
            if char.isdigit(): #4567
                digit = True

            elif char in "+-":
                if decimal or symbol or digit: # +-9 or --9
                    return False

                else:
                    symbol = True

            elif char in "eE":
                if not digit or exponent:
                    return False

                else:
                    decimal = digit = symbol = False
                    exponent = True

            elif char == ".":
                if decimal or exponent:
                    return False

                else:
                    decimal = True

            else:
                return False



        return digit
        