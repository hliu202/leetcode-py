# https://leetcode-cn.com/problems/minimum-size-subarray-sum/

# 前缀和
# 双指针

# j # 满足≥ s的，[j, i]个elements
from util.common_imports import *
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0

        pre_sum = nums[0]
        res = 0
        j = 0
        if pre_sum >= s: return 1

        for i in range(1, len(nums)):
            pre_sum += nums[i]
            while pre_sum >= s and j < i and pre_sum - nums[j] >= s:
                pre_sum -= nums[j]
                j += 1

            if res > 0:
                res = min(res, i - j + 1)
            elif pre_sum >= s:
                res = i - j + 1
        return res

# print(Solution().minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(s = 4, nums = [1,4,4]))