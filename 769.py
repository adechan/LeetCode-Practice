# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board) -> bool:
        valid = True

        # check rows
        for i in range(0, len(board)):
            valid_list = []
            for j in range(0, len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    valid_list.append(board[i][j])

            if len(valid_list) != len(set(valid_list)):
                valid = False
                break

        # check columns
        for i in range(0, len(board)):
            valid_list = []
            for j in range(0, len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    valid_list.append(board[j][i])

            if len(valid_list) != len(set(valid_list)):
                valid = False
                break

        # check sub-box
        for i in range(0, 3):
            for j in range(0, 3):
                valid_list = []

                for box_i in range(0, 3):
                    for box_j in range(0, 3):
                        if board[box_i + 3 * i][box_j + 3 * j] == ".":
                            continue
                        else:
                            valid_list.append(board[box_i + 3 * i][box_j + 3 * j])

                if len(valid_list) != len(set(valid_list)):
                    return False

        return valid

s = Solution()
board1 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board = [[".","2",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".","5",".","1"]
        ,[".",".",".",".",".",".","8","1","3"]
        ,["4",".","9",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".","2",".",".",".",".",".","."]
        ,["7",".","6",".",".",".",".",".","."]
        ,["9",".",".",".",".","4",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]]
print(s.isValidSudoku(board))