class Solution(object):
    def isNumber(self, s):
        decimal = exponent = digit = symbol = 0
        # decimal = .
        # exponent = eE
        # digit = 5667
        # symbol = +-

        for char in s:
            if char.isdigit():
                digit = True

            elif char in "+-":
                if digit or decimal or symbol: # If we have them after the symbol
                    return False
                else:
                    symbol = True

            elif char in 'eE':
                if not digit or exponent:
                    return False

                else:
                    digit = decimal = symbol = False
                    exponent = True

            elif char == '.': # decimal
                if decimal or exponent: # If decimal or exponent comes after decimal
                     return False

                else:
                    decimal = True

            else:
                return False

        return digit
