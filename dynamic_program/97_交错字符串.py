# f(i,j), s1 前 i 个, s2 前 j 个
from util.common_imports import *


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ns1, ns2 = len(s1), len(s2)
        if ns1 + ns2 != len(s3):
            return False

        dp = [[True] * (ns2 + 1) for _ in range(ns1 + 1)]

        # 边界条件
        for i in range(1, ns1 + 1):
            dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1]
        for j in range(1, ns2 + 1):
            dp[0][j] = dp[0][j - 1] and s3[j - 1] == s2[j - 1]

        for i in range(1, ns1 + 1):
            for j in range(1, ns2 + 1):
                dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
                    dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]
                )
        return dp[ns1][ns2]


print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(Solution().isInterleave(s1="", s2="", s3="a"))
print(Solution().isInterleave(s1="a", s2="", s3="c"))
