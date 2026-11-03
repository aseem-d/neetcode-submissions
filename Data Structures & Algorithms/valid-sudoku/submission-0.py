class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row:
                    return False
                
                row[board[i][j]] = 1
        
        for i in range(9):
            column = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in column:
                    return False
                
                column[board[j][i]] = 1
        
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                box_idx = (i//3) * 3 + (j//3)
            
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in boxes[box_idx]:
                    return False
            
                boxes[box_idx].add(board[i][j])
        
        return True

                

