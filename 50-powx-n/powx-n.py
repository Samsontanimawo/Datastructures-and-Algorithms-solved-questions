class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1

        elif n == 1:
            return x

        elif n == -1:
            return 1/x

        elif n%2==0:
            return self.myPow(x, n//2)**2

        else:
            return self.myPow(x, n//2) * self.myPow(x, n//2 + 1)

            
        