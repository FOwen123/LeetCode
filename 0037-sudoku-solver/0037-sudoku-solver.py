class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def check(row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                
                if board[i][col] == num:
                    return False
            
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
                
            return True
        
        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in "123456789":
                            if check(r, c, num):
                                board[r][c] = num

                                if solve(board):
                                    return True
                                board[r][c] = "."
                        return False
            return True
                            
        solve(board)
                    
            