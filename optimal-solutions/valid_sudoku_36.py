import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for i in range(0,9):
            for j in range(0,9):
                if(board[i][j] == "."):
                    continue
                if(board[i][j] in rows[i] or
                   board[i][j] in columns[j] or
                   board[i][j] in boxes[(i//3,j//3)]):
                    return False 
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[(i//3,j//3)].add(board[i][j])
        
        return True 