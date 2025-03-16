class Solution(object):

    def maxAreaOfIsland(self, grid):
        # If the grid is empty, return 0 (edge case)
        if not grid or not grid[0]:
            return 0

        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        max_area = 0  # Variable to store the maximum island area found

        def dfs(r, c):
            """
            Depth-First Search (DFS) function to explore the island starting at (r, c)
            """
            # Base case: If out of bounds or cell is water (0), return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # Mark the cell as visited by setting it to 0
            area = 1  # Start area count from this cell
            
            # Recursively explore all 4 directions (up, down, left, right)
            area += dfs(r+1, c)  # Move down
            area += dfs(r-1, c)  # Move up
            area += dfs(r, c+1)  # Move right
            area += dfs(r, c-1)  # Move left

            return area  # Return the computed area of this connected island

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is part of an island (1), start DFS
                if grid[r][c] == 1:
                    # Update max_area with the largest island found
                    max_area = max(max_area, dfs(r, c))

        return max_area  # Return the largest island area found