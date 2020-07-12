from util.common_imports import *

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        C = Counter(nums)
        ans = 0
        for k in C.keys():
            v = C[k]
            if v > 2:
                ans += v * (v-1) // 2
            elif v == 2:
                ans += 1
        return ans
print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))