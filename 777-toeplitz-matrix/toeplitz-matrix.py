class Solution:
    def isToeplitzMatrix(self, matrix):
        # Iterate through each row (except the last one)
        for row in range(len(matrix) - 1):
            # Iterate through each column (except the last one)
            for col in range(len(matrix[0]) - 1):
                # Check if the current element is not equal to the diagonal element
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    # If not equal, it's not a Toeplitz matrix
                    return False

        # If all elements passed the check, it's a Toeplitz matrix
        return True
