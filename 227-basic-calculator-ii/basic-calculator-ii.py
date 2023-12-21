class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        operation = "+"
        
        for char in s + "+":
            if char.isdigit():
                num = num * 10 + int(char)
                
            elif char in '+-*/':
                if operation == "+":
                    stack.append(num)

                elif operation == "-":
                    stack.append(-num)

                elif operation == "*":
                    stack[-1] *= num

                elif operation == "/":

                    # In Python 3, use integer division //
                    stack[-1] = int(stack[-1] / float(num))
                    
                operation = char
                num = 0
                
        return sum(stack)
