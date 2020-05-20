# https://leetcode-cn.com/problems/maximal-square/

# m = [["1","0","1","0","0"],
#      ["1","0","1","1","1"],
#      ["1","1","1","1","1"],
#      ["1","0","0","1","0"]]
# m = [["1"]]
m = [["0","0","0","1"]
    ,["1","1","0","1"]
    ,["1","1","1","1"]
    ,["0","1","1","1"]
    ,["0","1","1","1"]]

# y = len(m)
x = len(m[0])
dp = []

# dp[i][j] 包含(i,j)节点在内的，正方形的边长，不是正方形则为0
res = 0
for i, a in enumerate(m):
    dp.append([0] * x)
    for j, v in enumerate(a):
        if v == "1":
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                res = max(dp[i][j], res)
            else:
                dp[i][j] = 1
                res = max(res, 1)

print (res * res)

# 执行用时 :104 ms, 在所有 Python 提交中击败了53.97%的用户
# 内存消耗 :17.9 MB, 在所有 Python 提交中击败了100.00%的用户