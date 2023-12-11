# Anything raised to power 0 = 1
# Anything raised to -1 = 1/n
# Negative 
# Positive

class Solution(object):
    def myPow(self, x, n):
        
        if n == 0:
            return 1

        if n == 1:
            return x

        if n == -1:
            return 1/x
       
       # If n is even, pow(x, n) = pow(x, n/2) * pow(x, n/2).
        if n%2==0: # 2^4 = 2^2 X 2^2 = 
            return self.myPow(x, n//2) ** 2
            
# If n is odd, pow(x, n) = pow(x, n/2) * pow(x, n/2) * x.
        else: # Odd numbers = 2^5 = 2^4 X 2^1 = 2^2 X 2^2 X 2^1
            return self.myPow(x, n//2) * self.myPow(x, n//2 + 1)
        