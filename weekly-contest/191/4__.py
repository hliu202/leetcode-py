# 暴力枚举

import itertools
import math
from typing import *


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        def arrangement(nums: Sequence[int]):
            s = sum(nums)
            t = math.factorial(s)
            for b in nums:
                t //= math.factorial(b)
            return t

        def count(nums: Sequence[int]):
            return sum(b != 0 for b in nums)

        n = sum(balls) // 2
        total = arrangement(balls)
        ans = 0
        for left in itertools.product(*(range(b + 1) for b in balls)):
            if sum(left) != n:
                continue
            right = tuple(b - v for b, v in zip(balls, left))
            if count(left) == count(right):
                ans += arrangement(left) * arrangement(right)
        return ans / total

# 作者：sth4nothing
# 链接：https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/solution/python3-mei-ju-2372ms-by-sth4nothing/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print(Solution().getProbability(balls = [2,1,1]))
# print(Solution().getProbability(balls = [1,2,1,2]))