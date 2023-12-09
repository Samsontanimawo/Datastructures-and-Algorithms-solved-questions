class Solution:
    def isValidPalindrome(self, s, k):
        n = len(s)

        # Create a table to store the minimum deletions needed for substrings
        dp = [[0] * n for _ in range(n)]

        # Initialize the table for substrings of length 1
        for i in range(n):
            dp[i][i] = 0

        # Fill the table for substrings of length 2 and greater
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Check if the characters at the two ends are equal
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    # If characters are not equal, choose the minimum of deletions from either side and add 1
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

        # Check if the number of deletions needed is less than or equal to k
        return dp[0][n - 1] <= k

# Example usage:
#solution = Solution()
# print(solution.isValidPalindrome("abcdeca", 2))  # Output: True
# print(solution.isValidPalindrome("abbababa", 1))  # Output: True
