# https://leetcode-cn.com/problems/first-missing-positive/submissions/
# 置换，恢复成[1,x,3,y,5,...]

from util.common_imports import *

# class Solution:
#     def firstMissingPositive(self, nums):
#         n = len(nums)
#         for i,v in enumerate(nums):
#             next_v= v
#             while 0 < next_v <= n and i + 1 != next_v:
#                 if i + 1 == next_v: break
#                 tmp = nums[next_v - 1]
#                 if tmp != next_v:
#                     nums[next_v - 1] = next_v
#                     nums[i] = tmp

#                     next_v = tmp
#                 else: # 重复值，忽略
#                     nums[i] = n + 1
#                     break
#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1
#         return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


print(Solution().firstMissingPositive([1, 2, 0]))
print(Solution().firstMissingPositive([3, 4, -1, 1]))  # !持续替换，4 -> 1 -> ...
print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
print(Solution().firstMissingPositive([1, 1]))

