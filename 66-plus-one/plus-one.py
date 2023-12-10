class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        carry = 1  # Initialize carry to 1 to represent the increment

        for i in range(n - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10  # Update the current digit
            carry = total // 10  # Update the carry

        if carry:
            digits.insert(0, carry)  # If there is a carry left, insert a new digit at the beginning

        return digits