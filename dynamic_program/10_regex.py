# 我们用 f[i][j]f[i][j] 表示 ss 的前 ii 个字符与 pp 中的前 jj 个字符是否能够匹配。在进行状态转移时，我们考虑 pp 的第 jj 个字符的匹配情况：
# 链接：https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/

# f(i,j) 表示 s 前 i 个和 p 前 j 个匹配
# f(i,j) =
#  1. p[j] is alpha: f(i-1,j-1) and s[i] == p[j]
#  2. p[j] is *: f(i,j-2) (匹配 0 次) or: f(i-1,j-2) (s[i] = p[j-1]), ...
#     2.1 f[i-1][j] (扔掉 s[i]还能继续匹配) or f[i][j-2] （一个都不匹配) , s[i] = p[j-1]
#     2.2 f[i][j-2], s[i] ≠ p[j-1]
#  3. p[j] is .: match

# f[i][j] 和 s[i-1],p[j-1]对应
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matches(i, j):
            if i == 0:
                return False
            elif p[j - 1] == ".":
                return True
            else:
                return s[i - 1] == p[j - 1]

        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                elif matches(i, j):
                    f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


# print (Solution().isMatch(s = "mississippi",p = "mis*is*p*."))
print(Solution().isMatch(s="aab", p="c*a*b"))
