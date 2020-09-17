# https://leetcode-cn.com/problems/sudoku-solver/

from util.common_imports import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        allset = {'1','2','3','4','5','6','7','8','9'}
        N = 9

        # 当前值
        rows, columns, cubes = [], [], []

        update = True
        while update:
            for i in range(0, N):
                cur_row = set() # 第i行
                cur_col = set() # 第i列
                for j in range(0, N):
                    if board[i][j] != '.':
                        cur_row.add(board[i][j])
                    if board[j][i] != '.':
                        cur_col.add(board[j][i])

                rows.append(cur_row)
                columns.append(cur_col)

            for i in range(0, 3):
                cube_row = []
                for j in range(0, 3):
                    # 第i,j个方格
                    cur_cube = set()

                    for k in range(0, 3):
                        for l in range(0, 3):
                            if board[i*3+k][j*3+l] != '.':
                                cur_cube.add(board[i*3+k][j*3+l])
                    cube_row.append(cur_cube)

                cubes.append(cube_row)

            update = False
            for i in range(0, N):
                for j in range(0, N):
                    if board[i][j] == '.': # 看可能的取值
                        cur = rows[i] | columns[j] | cubes[i//3][j//3]
                        if len(cur) == 8:
                            board[i][j] = list(allset - cur)[0]

                            rows[i].add(board[i][j])
                            columns[j].add(board[i][j])
                            cubes[i//3][j//3].add(board[i][j])
                            update = True


# board = \
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]

board = \
[[".",".","9","7","4","8",".",".","."],
 ["7",".",".",".",".",".",".",".","."],
 [".","2",".","1",".","9",".",".","."],
 [".",".","7",".",".",".","2","4","."],
 [".","6","4",".","1",".","5","9","."],
 [".","9","8",".",".",".","3",".","."],
 [".",".",".","8",".","3",".","2","."],
 [".",".",".",".",".",".",".",".","6"],
 [".",".",".","2","7","5","9",".","."]]

Solution().solveSudoku(board)
print2D(board)

# 需要回溯
# ['.', '.', '9', '7', '4', '8', '.', '.', '.']
# ['7', '.', '.', '6', '.', '2', '.', '.', '.']
# ['.', '2', '.', '1', '.', '9', '.', '.', '.']
# ['.', '.', '7', '9', '8', '6', '2', '4', '1']
# ['2', '6', '4', '3', '1', '7', '5', '9', '8']
# ['1', '9', '8', '5', '2', '4', '3', '6', '7']
# ['.', '.', '.', '8', '6', '3', '.', '2', '.']
# ['.', '.', '.', '4', '9', '1', '.', '.', '6']
# ['.', '.', '.', '2', '7', '5', '9', '.', '.']
