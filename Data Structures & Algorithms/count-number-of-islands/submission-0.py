class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        islands = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or grid[r][c] == "0":
                return
            seen.add((r,c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    islands +=1
                    
        return islands