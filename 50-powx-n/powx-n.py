# X raise to power n

#      if      n    0  if n == even. E.g 2
#      if     X     1
#      if     X     -1
#             4/2  = 2 Return 2, 4//2^2
#             2
class Solution:
    def myPow(self, x, n):
        
        # Base case: x^0 = 1
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        # Handle negative exponent by recursively computing the reciprocal
        if n == -1:
            return 1/x
        
        # If n is even, x^n = (x^(n/2))^2
        if n%2 == 0:
            return self.myPow(x, n//2)**2
        
         # If n is odd, x^n = (x^(n//2))^2 * x
        else:
            return self.myPow(x, n//2) * self.myPow(x, n//2 + 1)