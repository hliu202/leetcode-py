# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n < 2:
#             return False

#         total = sum(nums)
#         maxNum = max(nums)
#         if total & 1:
#             return False

#         target = total // 2
#         if maxNum > target:
#             return False

#         dp = [[0] * (target + 1) for _ in range(n)]
#         for i in range(n):
#             dp[i][0] = True

#         dp[0][nums[0]] = True
#         for i in range(1, n):
#             num = nums[i]
#             for j in range(1, target + 1):
#                 if j >= num:
#                     dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
#                 else:
#                     dp[i][j] = dp[i - 1][j]

#         return dp[n - 1][target]

# https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/

# 给定一个只包含正整数的非空数组，判断是否可以从数组中选出一些数字，使得这些数字的和等于整个数组的元素和的一半。因此这个问题可以转换成「0-1 背包问题」。


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。