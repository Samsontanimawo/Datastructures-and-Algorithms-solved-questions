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

        if n%2==0:
            return self.myPow(x, n//2) ** 2

        else:
            return self.myPow(x, n//2) * self.myPow(x, n//2 + 1)
        