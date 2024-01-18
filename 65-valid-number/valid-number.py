class Solution(object):
    def isNumber(self, s):
       symbol = exponent = decimal = digit = False

       for char in s:
           if char.isdigit():
               digit = True

           elif char in "+-":
                if symbol or decimal or digit:
                    return False

                else:
                    symbol = True

           elif char in "eE":
                if not digit or exponent:
                    return False

                else:
                    digit = decimal = symbol = False
                    exponent = True

           elif char in ".":
                if decimal or exponent:
                    return False

                else:
                    decimal = True

           else:
                return False

       return digit