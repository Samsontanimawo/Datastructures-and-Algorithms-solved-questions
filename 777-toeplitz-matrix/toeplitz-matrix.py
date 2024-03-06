class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False

        return True

# O(MxN) Time and space