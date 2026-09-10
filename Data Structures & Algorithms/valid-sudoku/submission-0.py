class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] =='.':
                    continue
                if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[i//3*3+j//3]:
                    return False
                
                column[j].add(board[i][j])
                row[i].add(board[i][j])
                square[i//3*3+j//3].add(board[i][j])
        return True
                


                
            
