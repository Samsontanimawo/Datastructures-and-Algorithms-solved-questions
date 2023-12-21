class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        symbol = "+"
        
        for char in s + "+":
            if char.isdigit():
                num = num * 10 + int(char)
                
            elif char in '+-*/':
                if symbol == "+":
                    stack.append(num)
                elif symbol == "-":
                    stack.append(-num)
                elif symbol == "*":
                    stack[-1] *= num
                elif symbol == "/":
                    # In Python 3, use integer division //
                    stack[-1] = int(stack[-1] / float(num))
                    
                symbol = char
                num = 0
                
        return sum(stack)
