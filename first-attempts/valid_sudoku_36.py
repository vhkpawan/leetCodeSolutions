""" --------------------------------------------------------------------------------------------- 
SCRIPT META DATA 
Name: Pawan HK 
Date: 08/29/2025 
ID: 36
Problem: Valid Sudoku
Difficulty: Medium 
Time: 00:36:59
Time Complexity: N^2
Runtime: 2ms 
Beats: 85.78%
Memory: 17.98MB 
MBeats: 24.98%
Status: COMPLETED
END DATA
--------------------------------------------------------------------------------------------- """

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set default empty 
        col_seen = []
        row_seen = []
        box_seen = []

        # row check 
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j] not in row_seen):
                    if(board[i][j] == "."):
                        continue
                    row_seen.append(board[i][j])
                else:
                    return False
            row_seen = []
        
        #col checks
        for i in range(len(board[0])):
            for j in range(len(board)):
                if(board[j][i] not in col_seen):
                    if(board[j][i] == "."):
                        continue
                    col_seen.append(board[j][i])
                else:
                    return False
            col_seen = []

        # 3x3 test
        for i in range(3):   
            for j in range(3):
                for m in range(i*3, i*3 + 3):    
                    for n in range(j*3, j*3 + 3):
                        if(board[m][n] not in box_seen):
                            if(board[m][n] == "."):
                                continue
                            box_seen.append(board[m][n])
                        else:
                            return False
                box_seen = []

        return True