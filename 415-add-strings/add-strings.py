class Solution(object):
    def addStrings(self, num1, num2):
        
        num1LastIndex = len(num1)-1
        num2LastIndex = len(num2)-1
        carry = 0
        result = []
        
        while num1LastIndex >= 0 or num2LastIndex >= 0:
            x = int(num1[num1LastIndex] if num1LastIndex >= 0 else 0)
            y = int(num2[num2LastIndex] if num2LastIndex >= 0 else 0)
            sum = x + y + carry
            carry = sum / 10
            
            result.append(str(sum % 10))
            num1LastIndex -=1
            num2LastIndex -=1
            
        if carry:
            result.append(str(carry))
            
        return ''.join(result[::-1])