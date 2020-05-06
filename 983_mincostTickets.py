

# https://leetcode-cn.com/problems/minimum-cost-for-tickets/

days = [1,2,3,4,5,6,7,8,9,10,30,31]  # [1,4,6,7,8,20]
costs = [2,7,15]

# https://leetcode-cn.com/problems/minimum-cost-for-tickets/solution/xiong-mao-shua-ti-python3-dong-tai-gui-hua-yi-do-2/
# 动态规划问题最重要是3步：
    # 明确创建怎样的dp数组
    # 初始化dp数组
    # 明确动态转移方程

dp = [0] * (days[-1] + 1)

cur_idx = 0;
for i in range(1, len(dp)):
    if i == days[cur_idx]:
        cur_idx += 1

        dp[i] = min(costs[0] + dp[i-1],
                    costs[1] + dp[max(0, i - 7)],
                    costs[2] + dp[max(0, i - 30)])
    else:
        dp[i] = dp[i-1]

print (dp[-1])
