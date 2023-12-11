class Solution(object):
    def isNumber(self, s):

        decimal = digit = exponent = symbol = False

        for char in s:
            if char.isdigit():
                digit = True # 123

            elif char in "+-":
                if digit or symbol or decimal:
                    return False

                else:
                    symbol = True

            elif char in "eE":
                if not digit or exponent:
                    return False

                else:
                    digit = symbol = decimal = False
                    exponent = True

            elif char == ".":
                if decimal or exponent:
                    return False

                else:
                    decimal = True

            else:
                return False


        return digit