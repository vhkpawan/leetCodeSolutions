from typing import List
# Did not attempt, first attempt after watching a hint -> runtime exceeded 
"""
Box Offset Calculation: 
- For a cell at (row, col), its 3x3 box starts at:
  sub_box_row = (row // 3) * 3
  sub_box_col = (col // 3) * 3
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_board_valid(board, row, col, num_char):
            # row check
            for c in range(0, 9):
                if board[row][c] == num_char:
                    return False 

            # col check 
            for r in range(0, 9):
                if board[r][col] == num_char:
                    return False 

            # box check 
            sub_box_row = (row // 3) * 3
            sub_box_col = (col // 3) * 3
            for r in range(sub_box_row, sub_box_row + 3):
                for c in range(sub_box_col, sub_box_col + 3):
                    if board[r][c] == num_char:
                        return False

            return True

        def backtracking_implementation(board):
            for r in range(0, 9):
                for c in range(0, 9):
                    if board[r][c] == ".":
                        # now we know it's an empty cell 
                        for i in range(1, 10):
                            # check every possible i for a solution 
                            # first prune the tree 
                            num_char = str(i)
                            if is_board_valid(board, r, c, num_char):
                                board[r][c] = num_char
                                if backtracking_implementation(board):
                                    return True
                                else:
                                    board[r][c] = "."  # undo
                        # tried all the numbers, the route didn't work 
                        return False
            return True
        
        backtracking_implementation(board)
