# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
from util.common_imports import *


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        self.right = [nums[-1]]
        ans = []

        def insert(cur):
            l, r = 0, len(self.right) - 1
            while l < r:
                mid = (l + r) // 2
                if self.right[mid] < cur:
                    l = mid + 1
                else:
                    r = mid
            self.right.insert(l, cur)
            return l

        for i in range(len(nums) - 1, -1, -1):
            a = insert(nums[i])
            ans.append(a)
        return ans[::-1]


print(Solution().countSmaller([5, 2, 6, 1]))

