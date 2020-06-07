
# dp[i][j]: 第 0 到 i 个房子，target 为 j 的最小 cost
#  = min(dp[i-1][j] + sameColor, dp[i-1][j-1] + differentColor)
# 求最小 dp[m][target]

from util.common_imports import *

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp = [-1] * m for _ in range(target+1)

        oldColors = Counter(houses)
        n_house = len(houses)
        minT = len(oldColors) - 1  if 0 in oldColors else len(oldColors)

        coloredIdx = deque()
        if minT > 0:
            for i in range(len(houses))
                if houses[i] != 0:
                    coloredIdx.append(i)

        for t in range(minT, target+1):
            if t == minT and minT > 0:
                curColorIdx = coloredIdx.popleft()
                for i in n_house:
                    if i == curColorIdx and coloredIdx:
                        curColorIdx = coloredIdx.popleft()
                    dp[i]
                if i == 0: # 1st color
                    if houses[i] == 0: # no color
                        dp[0][1] = min(cost[0])
                        houses[i] = cost.index(dp[0][1])
                    else:
                        dp[0][1] = 0
                else:
                    if houses[i] == 0:
                        dp[i][1] = cost[i][houses[i-1]]
                        houses[i] = houses[i-1]
                    elif houses[i] != houses[i-1]:
                        break


print(Solution().minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
