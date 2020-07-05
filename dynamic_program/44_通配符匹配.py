# https://leetcode-cn.com/problems/wildcard-matching/

# dp(i,j) p[:i]和s[:j]是否匹配
# dp(i,j) =
#   1. dp[i-1][j-1] && p[i] == s[i] (include p[i]='?')
#   2. dp[i-1][j] && p[i] == '*'


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp = [[False] * (ns + 1) for _ in range(np + 1)]
        dp[0][0] = True  # 都是空

        def match(c1, c2):
            return c1 == c2 or c1 == "?"

        for i in range(1, np + 1):
            dp[i][0] = p[i - 1] == "*" and dp[i - 1][0]  # 匹配s=''

            for j in range(1, ns + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and match(p[i - 1], s[j - 1])
                # !不能提前退出：E.g. 从dp[1][1] -> dp[2][2]这条对角线...
                # if not dp[i][j]:
                #     break

        return dp[np][ns]


print(Solution().isMatch("aa", "*"))
print(Solution().isMatch("cb", "?a"))
print(Solution().isMatch("cb", "*?"))
print(Solution().isMatch("cb", "*b"))
print(Solution().isMatch("cb", "?b"))

