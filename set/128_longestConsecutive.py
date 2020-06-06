# https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/

from util.common_imports import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if num - 1 not in num_set: # start a chain
                cur = 1

                while num + 1 in num_set:
                    num += 1
                    cur += 1

                res = max(res, cur)

        return res

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))