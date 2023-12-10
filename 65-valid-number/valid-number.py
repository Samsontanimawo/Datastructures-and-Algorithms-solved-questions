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
                if not digit or exponent:
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
