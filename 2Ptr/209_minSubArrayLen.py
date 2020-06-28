# https://leetcode-cn.com/problems/minimum-size-subarray-sum/

# j # 满足≥ s的，[j, i]个elements
from util.common_imports import *
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0

        sum = nums[0]
        res = 0
        j = 0
        if sum >= s: return 1

        for i in range(1, len(nums)):
            sum += nums[i]
            while sum >= s and j < i and sum - nums[j] >= s:
                sum -= nums[j]
                j += 1

            if res > 0:
                res = min(res, i - j + 1)
            elif sum >= s:
                res = i - j + 1
        return res

# print(Solution().minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(s = 4, nums = [1,4,4]))