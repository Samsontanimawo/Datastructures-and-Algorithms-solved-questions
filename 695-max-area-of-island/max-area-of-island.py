class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        This function computes the maximum area of an island in a given grid.
        An island consists of connected 1s (land), and connections are 4-directional
        (up, down, left, right). We use DFS with a 'seen' set to track visited cells.
        """

        seen = set()  # Set to track visited cells

        def area(r, c):
            """
            Recursive DFS function to calculate the area of an island.
            """
            # Base case: If the current cell is out of bounds OR
            # already visited OR is water (0), return 0.
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])  # Check bounds
                    and (r, c) not in seen  # Ensure cell is not visited
                    and grid[r][c]):  # Ensure cell is land (1)
                return 0

            seen.add((r, c))  # Mark cell as visited

            # Explore all 4 directions (down, up, right, left)
            return (1 + area(r+1, c) +  # Move Down
                    area(r-1, c) +  # Move Up
                    area(r, c-1) +  # Move Left
                    area(r, c+1))  # Move Right

        # Compute the maximum island area by iterating over the grid
        return max(area(r, c) 
                   for r in range(len(grid)) 
                   for c in range(len(grid[0])))
        
# Example test cases
solution = Solution()

grid1 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

grid2 = [[0,0,0,0,0,0,0,0]]

print(solution.maxAreaOfIsland(grid1))  # Output: 6
print(solution.maxAreaOfIsland(grid2))  # Output: 0
