from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mp = defaultdict(set)
        col_mp = defaultdict(set)
        mat_mp = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in row_mp[i]: return False
                if board[i][j] in col_mp[j]: return False
                if board[i][j] in mat_mp[(i//3, j//3)]: return False

                row_mp[i].add(board[i][j])
                col_mp[j].add(board[i][j])
                mat_mp[(i//3, j//3)].add(board[i][j])
        return True