from util.common_imports import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nx, ny = len(grid[0]) + 1, len(grid) + 1
        dp = [[float("inf")] * nx for _ in range(ny)]
        dp[0][0], dp[0][1], dp[1][0] = 0, 0, 0

        for y in range(1, ny):
            for x in range(1, nx):
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + grid[y - 1][x - 1]

        return dp[ny - 1][nx - 1]


# print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum([[1,2,5],[3,2,1]]))
