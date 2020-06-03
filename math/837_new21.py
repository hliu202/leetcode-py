# https://leetcode-cn.com/problems/new-21-game/solution/xin-21dian-by-leetcode-solution/

# 动态规划 + 反序

# 爱丽丝获胜的概率只和下一轮开始前的得分有关，因此根据得分计算概率。
# 令 dp[x]dp[x] 表示从得分为 xx 的情况开始游戏并且获胜的概率，目标是求 dp[0]dp[0] 的值。

# 还能抓牌的最大点数是多少: K-1
# f(16) = (1 x 5 + 0 x 5) / 10 # 10个点数，的获胜概率
# f(15) = (1*f(16) + 1 x 5 + 0 x 4) / 10

# 转移方程： f(x) = (f(x+1) + ... + f(x+w)) / w
# f(x-1) = (f(x) + ... + f(x+w-1)) / w
# f(x-1) - f(x) = (f(x) - f(x+w)) / w

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W # 还能抓牌的最大点数
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]