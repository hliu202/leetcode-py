from util.common_imports import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ny = len(board)
        if ny <= 2:
            return
        nx = len(board[0])
        if nx <= 2:
            return

        keep = set()
        for x in range(nx):
            if board[0][x] == "O":
                yy = 1
                while yy < ny - 1:
                    if board[yy][x] == "O":
                        keep.add((yy, x))
                        yy += 1
                    else:
                        break
            if board[ny - 1][x] == "O":
                yy = ny - 2
                while yy > 0:
                    if board[yy][x] == "O":
                        keep.add((yy, x))
                        yy -= 1
                    else:
                        break
        for y in range(ny):
            if board[y][0] == "O":
                xx = 1
                while xx < nx - 1:
                    if board[y][xx] == "O":
                        keep.add((y, xx))
                        xx += 1
                    else:
                        break
            if board[y][nx - 1] == "O":
                xx = nx - 2
                while xx > 0:
                    if board[y][xx] == "O":
                        keep.add((y, xx))
                        xx -= 1
                    else:
                        break

        def toAdd(i, j):
            if i + 1 != ny - 1 and (i + 1, j) in keep:
                return True
            if i - 1 != 0 and (i - 1, j) in keep:
                return True
            if j + 1 != nx - 1 and (i, j + 1) in keep:
                return True
            if j - 1 != 0 and (i, j - 1) in keep:
                return True

        while True:
            changed = False
            for i in range(1, ny - 1):
                for j in range(1, nx - 1):
                    if board[i][j] == "O" and (i, j) not in keep and toAdd(i, j):
                        changed = True
                        keep.add((i, j))
            if not changed:
                break

        for i in range(1, ny - 1):
            for j in range(1, nx - 1):
                if board[i][j] == "O" and (i, j) not in keep:
                    board[i][j] = "X"


# IN = [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"],
# ]
IN = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
Solution().solve(IN)
print(IN)

