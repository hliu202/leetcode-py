# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
from util.common_imports import *


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        right = [nums[-1]]
        ans = []

        def insert(cur):
            l, r = 0, len(right) - 1
            while l < r:
                mid = (l + r) // 2
                if right[mid] < cur:
                    l = mid + 1
                else:
                    r = mid
            right.insert(l, cur)
            return l

        for i in range(len(nums) - 1, -1, -1):
            a = insert(nums[i])
            ans.append(a)
        return ans[::-1]


print(Solution().countSmaller([5, 2, 6, 1]))

# class Solution:
# def countSmaller(self, nums: List[int]) -> List[int]:
#     sortns = []
#     res = []
#     for n in reversed(nums):
#         idx = bisect.bisect_left(sortns, n)
#         res.append(idx)
#         sortns.insert(idx, n)
#     return res[::-1]
