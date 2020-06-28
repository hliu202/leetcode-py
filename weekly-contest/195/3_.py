from util.common_imports import *

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        j = n - 1
        sum = [0] * n

        for i in range(n):
            while nums[i] + nums[j] > target and j > i:
                j -= 1
            if j == i:
                if nums[i] + nums[j] <= target:
                    res += 1
                return res % (1000000000 + 7)
            
            num_between = j - i - 1
            if i == 0:
                sum[0] = 2 # special {num[i]}
                for k in range(1, num_between + 1):
                    sum[k] = (sum[k-1] + pow(2, k)) % (1000000000 + 7)
            res += sum[num_between]
        
        return res % (1000000000 + 7)

print(Solution().numSubseq(nums = [2,3,3,4,6,7], target = 12))
print(Solution().numSubseq(nums = [5,2,4,1,7,6,8], target = 16))
print(Solution().numSubseq(nums = [3,5,6,7], target = 9))

# 超出时间限制