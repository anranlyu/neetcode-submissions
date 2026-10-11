class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pacific)            # top row
            dfs(rows - 1, c, atlantic)    # bottom row
        for r in range(rows):
            dfs(r, 0, pacific)            # left column
            dfs(r, cols - 1, atlantic)    # right column

        return [[r, c] for r, c in pacific & atlantic]
