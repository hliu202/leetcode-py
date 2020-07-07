# https://leetcode-cn.com/problems/unique-paths-ii/

# f(i,j) = f(i-1,j) + f(i,j-1)
from util.common_imports import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        ny, nx = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ny - 1][nx - 1] == 1:
            return 0
        dp = [[0] * nx for _ in range(ny)]

        def get(yy, xx):
            if yy > 0 and xx > 0:
                return dp[yy - 1][xx] + dp[yy][xx - 1]
            if yy > 0:
                return dp[yy - 1][xx]
            if xx > 0:
                return dp[yy][xx - 1]
            return 1  # 开始

        for y in range(ny):
            for x in range(nx):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = get(y, x)
        return dp[ny - 1][nx - 1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

print(Solution().uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]))

