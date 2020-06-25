# https://leetcode-cn.com/problems/3sum-closest/
from util.common_imports import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float("inf")
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            cur_target = target - nums[i]

            while j < k:
                cur_real = nums[j] + nums[k]
                res = (
                    cur_real + nums[i]
                    if abs(cur_real + nums[i] - target) < abs(res - target)
                    else res
                )
                if cur_real < cur_target:
                    j += 1
                elif cur_real > cur_target:
                    k -= 1
                else:
                    return target

        return res


print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))

