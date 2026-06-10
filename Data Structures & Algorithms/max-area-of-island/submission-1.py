class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_island = 0


        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            current_area = 1

            current_area += dfs(r + 1, c)
            current_area += dfs(r - 1, c)
            current_area += dfs(r, c + 1)
            current_area += dfs(r, c - 1)
            return current_area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_island = max(max_island, area)
        return max_island