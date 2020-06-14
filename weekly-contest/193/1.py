class Solution:
    def runningSum(self, nums):
        res = [0] * len(nums)
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            res[i] = cur
        return res
print(Solution().runningSum(nums = [3,1,2,10,1]))