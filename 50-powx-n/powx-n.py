# X raise to power n

#      if      n    0  if n == even. E.g 2
#      if     X     1
#      if     X     -1
#             4/2  = 2 Return 2, 4//2^2
#             2
class Solution:
    def myPow(self, x, n):
        
        if n < 0:
            x = 1/x
            n = -n

        result = 1.0

        while n>0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result