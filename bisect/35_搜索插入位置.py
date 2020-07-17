import bisect
from util.common_imports import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
print(Solution().searchInsert([1, 3, 5, 6], 0))
print(Solution().searchInsert([1, 3, 5, 6], 3))

