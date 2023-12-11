class Solution:
    def isNumber(self, s):
        # Initialize flags for different components of a number
        digit = decimal = symbol = exponent = False
        
        # Iterate through each character in the input string
        for char in s:
            # Check if the character is a digit
            if char.isdigit():
                digit = True
                
            # Check if the character is a symbol (+ or -)
            elif char in '+-':
                # Symbols are only allowed at the beginning or after an 'e'/'E'
                if digit or decimal or symbol:
                    return False
                else:
                    symbol = True
                
            # Check if the character is an 'e' or 'E' for exponent notation
            elif char in 'Ee':
                # 'e'/'E' should come after at least one digit and only once
                if not digit or exponent: # If not digit but exponent eeE. It should be 9e
                    return False
                else:
                    # Reset flags for digit, decimal, symbol, and set exponent flag
                    digit = decimal = symbol = False
                    exponent = True
                
            # Check if the character is a dot (decimal point)
            elif char == '.':
                # Dot is only allowed once and before an exponent
                if decimal or exponent:
                    return False
                else:
                    decimal = True
            
            # If the character is none of the valid characters, it's not a valid number
            else:
                return False
            
        # Check if at least one digit is present
        return digit

# Example usage:
sol = Solution()

# Test the examples
#print(sol.isNumber("2"))         # Output: True
#print(sol.isNumber("0089"))      # Output: True
#print(sol.isNumber("-0.1"))       # Output: True
#print(sol.isNumber("3."))         # Output: True
#print(sol.isNumber(".1"))         # Output: True
#print(sol.isNumber("1e3"))        # Output: True
#print(sol.isNumber("3e+7"))       # Output: True
#print(sol.isNumber("+6e-1"))      # Output: True
#print(sol.isNumber("53.5e93"))    # Output: True
#print(sol.isNumber("-123.456e789"))# Output: True
#print(sol.isNumber("abc"))        # Output: False
#print(sol.isNumber("1a"))         # Output: False
#print(sol.isNumber("1e"))         # Output: False
#print(sol.isNumber("e3"))         # Output: False
#print(sol.isNumber("99e2.5"))     # Output: False
#print(sol.isNumber("--6"))        # Output: False
#print(sol.isNumber("-+3"))        # Output: False
#print(sol.isNumber("95a54e53"))   # Output: False
