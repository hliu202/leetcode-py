#https://leetcode-cn.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
            if nums[i] == k:
                res += 1

        if len(nums) < 2:
            return res

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                dp[i][j] = dp[i][j-1] + nums[j]
                if dp[i][j] == k:
                    res += 1
        return res

print (Solution().subarraySum([1,1,1], 2))