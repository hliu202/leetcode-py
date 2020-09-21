class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        ncow = len(grid)
        ncol = len(grid[0])

        pos = [[None] * ncol for _ in range(0,ncow)] # 最大非负
        neg = [[None] * ncol for _ in range(0,ncow)] # 最小负数

        for j in range(0, ncol):
            # 0 row
            if j == 0:
                if grid[0][0] >= 0:
                    pos[0][0] = grid[0][0]
                else:
                    neg[0][0] = grid[0][0]
            else:
                if grid[0][j-1] == 0 or grid[0][j] == 0:
                    pos[0][j] = 0
                    neg[0][j] = None
                else:
                    if grid[0][j] > 0:
                        if pos[0][j-1]:
                            pos[0][j] = pos[0][j-1] * grid[0][j]
                        if neg[0][j-1]:
                            neg[0][j] = neg[0][j-1] * grid[0][j]
                    else: # negtive
                        if pos[0][j-1]:
                            neg[0][j] = pos[0][j-1] * grid[0][j]
                        if neg[0][j-1]:

        for i in range(0,ncow):
            for j in range(0,ncol):
                if i == 0:
                    if j == 0:
                        if grid[0][j] >= 0:
                            pos[0][0] = grid[0][0]
                        else:
                            neg[0][0] = grid[0][0]
                    else:
                        if grid[0][j] > 0:
                            if grid[0][j-1] >= 0:
                                pos[0][0] = grid[0][j-1] * grid[0][j]
