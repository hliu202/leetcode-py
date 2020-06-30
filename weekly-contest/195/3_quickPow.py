from util.common_imports import *


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        res = 0
        sum = [0] * n

        M = 10**9 + 7
        for i in range(n):
            while nums[i] + nums[j] > target and j > i:
                j -= 1
            if j == i:
                if nums[i] + nums[j] <= target:
                    res += 1
                return res % M

            num_between = j - i - 1
            if i == 0:
                prePow=1
                sum[0] = 2  # special {num[i]}
                for k in range(1, num_between + 1):
                    prePow <<= 1 # !2^n，调用pow会超时
                    sum[k] = (sum[k - 1] + prePow) % M
            res += sum[num_between]

        return res % (1000000000 + 7)


print(Solution().numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))
print(Solution().numSubseq(nums=[5, 2, 4, 1, 7, 6, 8], target=16))
print(Solution().numSubseq(nums=[3, 5, 6, 7], target=9))

# 执行用时：3976 ms, 在所有 Python3 提交中击败了100.00%的用户
# 内存消耗：22.5 MB, 在所有 Python3 提交中击败了100.00%的用户
