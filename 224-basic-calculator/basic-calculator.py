class Solution(object):
    def calculate(self, s):
        
        result = currentSum = 0
        symbol = 1
        stack = []

        
        
        for char in s:
            if char.isdigit():
                currentSum = currentSum *10+int(char)
                
            elif char in '+-':
                result += (currentSum * symbol)
                currentSum = 0
                
                if char == '-':
                    symbol = -1
                
                else:
                    symbol = 1
                    
            elif char == '(':
                stack.append(result)
                stack.append(symbol)
                result = 0
                symbol = 1
                
            elif char == ')':
                result += (currentSum * symbol)
                result *= stack.pop()
                result += stack.pop()
                currentSum = 0
            
        return result + (currentSum * symbol)