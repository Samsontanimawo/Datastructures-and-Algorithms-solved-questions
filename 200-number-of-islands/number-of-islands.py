class Solution:
    def numIslands(self, grid):
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark current cell as visited
            # Explore adjacent cells
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an unvisited island
                    num_islands += 1
                    dfs(grid, i, j)  # Explore and mark all connected land cells as visited
        return num_islands