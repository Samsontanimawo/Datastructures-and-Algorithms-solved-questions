class Solution:
    def findDiagonalOrder(self, matrix):
        
        rows, cols, row, col, result = len(matrix), len(matrix[0]), 0, 0, []
        
        for index in range(rows * cols):
            result.append(matrix[row][col])
            
            if (row + col) % 2 == 0:
                if col == (cols - 1):
                    row +=1
                    
                elif row == 0:
                    col +=1
                    
                else:
                    row -=1
                    col +=1
            
            else:
                if row == (rows - 1):
                    col +=1
                
                elif col == 0:
                    row +=1
                
                else:
                    row +=1
                    col -=1
        return result 
        