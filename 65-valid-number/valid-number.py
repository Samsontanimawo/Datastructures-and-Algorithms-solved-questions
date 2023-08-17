class Solution:
    def isNumber(self, s):
        
        digit = decimal = exponent = symbol = False
        
        for char in s:
            if char.isdigit():
                digit = True
                
                
            elif char in '+-':
                if digit or symbol or decimal:
                    return False
                
                else:
                    symbol = True
                    
            elif char in 'Ee':
                if not digit or exponent:
                    return False
                
                else:
                    exponent = True
                    digit = False
                    decimal = False
                    symbol = False
                    
            elif char == '.':
                if decimal or exponent:
                    return False
                
                else:
                    decimal = True                
                
                
                
            else:
                return False
            
        return digit