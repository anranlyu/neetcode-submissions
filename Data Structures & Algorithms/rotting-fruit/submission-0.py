class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            r,c = q.popleft()
            for dr,dc in direction:
                nr , nc = r+dr,c+dc
                if nr<rows and nr>=0 and nc<cols and nc>=0 and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c]+1
                    fresh -=1
                    q.append((nr,nc))
                    minutes = max(minutes,grid[nr][nc]-2)
        
        return -1 if fresh else minutes
                
        