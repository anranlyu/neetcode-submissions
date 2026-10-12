class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows , cols = len(board), len(board[0])
        connect = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if r < 0 or r >= rows or c <0 or c >= cols or board[r][c] == 'X' or (r,c) in connect :
                return
            connect.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
        
        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1,j)
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in connect:
                    board[r][c] = 'X'
