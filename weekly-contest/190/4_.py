# https://leetcode-cn.com/contest/weekly-contest-190/problems/max-dot-product-of-two-subsequences/

# 动态规划

# 第一种想法： dp[i][j]的含义是以nums1[i]和nums2[j]结尾的子序列的最大点积。 X
# 第二种想法：dp[i][j]的含义是到nums1[i]和nums2[j]为止的子序列的最大点积。 

# 1. dp[i][j] 为前 i 和前 j 个最大点集
#    dp[0][0] 为 A[0] * B[0]
# 2. dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j]+A[i+1]*B[j+1])



class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a, b = nums1, nums2
        if max(a)<0<min(b): return max(a)*min(b)
        if max(b)<0<min(a): return max(b)*min(a)
        n, m = len(a), len(b)
        f = [[0]*(m+1) for _ in range(n+1)] # 哨兵, f[1][1]为开始
        for i in range(n):
            for j in range(m):
                f[i+1][j+1] = max(f[i][j+1], f[i+1][j], f[i][j]+a[i]*b[j])
        return f[n][m]

print(Solution().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))