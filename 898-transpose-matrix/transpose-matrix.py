class Solution(object):
    def transpose(self, matrix):
    # Get the number of rows and columns in the original matrix
        rows, cols = len(matrix), len(matrix[0])

    # Create a new matrix with swapped rows and columns
        transposed_matrix = [[0] * rows for _ in range(cols)]

    # Iterate through the original matrix and fill in the transposed_matrix
        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]

        return transposed_matrix
        