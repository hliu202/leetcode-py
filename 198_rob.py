# https://leetcode-cn.com/problems/house-robber/
from util.common_imports import *

# dp + 滚动数组(2)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        A0 = 0 # 不包含 i 的最大值
        A1 = nums[0] # 包含 i 的值

        for i in range(1, len(nums)):
            tmp = A0
            A0 = max(A1, A0)
            A1 = max(A1 - nums[i-1] + nums[i], tmp + nums[i])
        
        return max(A0, A1)

print(Solution().rob([]))
print(Solution().rob([1,2]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,1,1,3]))
print(Solution().rob([2,7,9,3,1]))

