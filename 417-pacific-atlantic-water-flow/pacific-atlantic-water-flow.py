class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Directions for moving: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c, visited):
            # Mark the current cell as visited
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and ensure water can flow (height must be >= current)
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        
        # 2D lists to track the cells that can reach the Pacific and Atlantic Oceans
        pacific_visited = [[False] * n for _ in range(m)]
        atlantic_visited = [[False] * n for _ in range(m)]
        
        # Start DFS from the Pacific and Atlantic borders
        for i in range(m):
            dfs(i, 0, pacific_visited)  # Pacific Ocean: leftmost column
            dfs(i, n - 1, atlantic_visited)  # Atlantic Ocean: rightmost column
        
        for j in range(n):
            dfs(0, j, pacific_visited)  # Pacific Ocean: top row
            dfs(m - 1, j, atlantic_visited)  # Atlantic Ocean: bottom row
        
        # Find cells that can reach both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])
        
        return result
