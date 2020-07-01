# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/ni-de-yi-fu-wo-ba-liao-zui-chang-gong-gong-zi-xu-l/

# dp(i,j) = dp(i-1,j-1) + 1 if A[i]==A[j]

# 1. 暴力解法
# 2. 用dp优化

from util.common_imports import *

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        na, nb = len(A), len(B)
        dp = [[0] * (nb+1) for _ in range(na+1)]
        ans = 0

        for i in range(0, len(A)):
            for j in range(0, len(B)):
                cur = dp[i][j] + 1 if A[i] == B[j] else 0
                dp[i+1][j+1] = cur
                ans = max(cur, ans)
        return ans

print (Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))
