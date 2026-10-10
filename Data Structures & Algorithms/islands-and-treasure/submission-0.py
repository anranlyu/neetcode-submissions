class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows,cols = len(grid),len(grid[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r,c = q.popleft()
            for dr,dc in direction:
                nr , nc = r+dr, c+ dc
                if nr < rows and nr >= 0 and nc<cols and nc>=0  and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c]+1
                    q.append((nr,nc))
                
        


            