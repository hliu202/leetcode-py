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
    ,["0","1","1","1"]]  # wrong

# y = len(m)
x = len(m[0])
dp = []

# dp[i][j] 包含(i,j)节点在内的，正方形的边长，不是正方形则为0
res = 0
for i, a in enumerate(m):
    dp.append([0] * x)
    for j, v in enumerate(a):
        if v == "1":
            if i > 0 and j > 0 and dp[i - 1][j - 1] > 0 and dp[i - 1][j] > 0 and dp[i][j -  1] > 0:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(dp[i][j], res)
            else:
                dp[i][j] = 1
                res = max(res, 1)

print (res * res)
