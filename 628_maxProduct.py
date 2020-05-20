# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/

from typing import List
import sys

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max0 = -sys.maxsize-1
        max1 = -sys.maxsize-1
        max2 = -sys.maxsize-1
        min0 = sys.maxsize
        min1 = sys.maxsize

        for v in nums:
            if v > max0:
                max2 = max1
                max1 = max0
                max0 = v
            elif v > max1:
                max2 = max1
                max1 = v
            elif v > max2:
                max2 = v

            if v < min0:
                min1 = min0
                min0 = v
            elif v < min1:
                min1 = v
        return max(max0*max1*max2, max0*min0*min1)

print(Solution().maximumProduct([1,2,3,4]))
print(Solution().maximumProduct([1,2,3]))