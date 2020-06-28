# nums[i,j] nums[i] + nums[j] <= N:
from util.common_imports import *

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            if 2 * nums[i] > target:
                break

            for j in range(i, n):
                if nums[i] + nums[j] > target:
                    break

                bt = j - i - 1
                if bt > 0:
                    # 二项式定理 2^n
                    res += pow(2, bt)
                else:
                    res += 1
        return res % (1000000000 + 7)
print(Solution().numSubseq(nums = [2,3,3,4,6,7], target = 12))
print(Solution().numSubseq(nums = [5,2,4,1,7,6,8], target = 16))
# 超时