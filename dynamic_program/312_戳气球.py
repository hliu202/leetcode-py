# https://leetcode-cn.com/problems/burst-balloons/

# 记忆化搜索
# 于是我们倒过来看这些操作，将全过程看作是每次添加一个气球。
# 我们定义方法 solve，令 solve(i,j) 表示将开区间 (i,j) 内的位置全部填满气球能够得到的最多硬币数。由于是开区间，因此区间两端的气球的编号就是 ii 和 jj，对应着 \textit{val}[i]val[i] 和 \textit{val}[j]val[j]。


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
