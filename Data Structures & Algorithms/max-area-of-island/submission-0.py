class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid),len(grid[0])
        max_area = 0
        seen = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0 or (r,c) in seen:
                return 0
            
            seen.add((r,c))
            total = 1
            for dr,dc in direction:
                total+= dfs(r+dr,c+dc)
            return total
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area,dfs(r,c))
        return max_area

        