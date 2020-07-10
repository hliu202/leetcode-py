# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


# 我们用 f[i]f[i] 表示第 ii 天结束之后的「累计最大收益」。根据题目描述，由于我们最多只能同时买入（持有）一支股票，并且卖出股票后有冷冻期的限制，
# !因此我们会有三种不同的状态：
# 我们目前持有一支股票，对应的「累计最大收益」记为 f[i][0]f[i][0]；
# 我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 f[i][1]f[i][1]；
# 我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]f[i][2]。


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])

