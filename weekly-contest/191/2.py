from util.common_imports import *


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        nh = len(horizontalCuts)
        nv = len(verticalCuts)
        horizontalCuts.sort()
        verticalCuts.sort()
        h = max(horizontalCuts[0], h - horizontalCuts[-1])
        v = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, nh):
            h = max(h, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, nv):
            v = max(v, verticalCuts[i] - verticalCuts[i - 1])
        return h * v % (1000000007)

print(Solution().maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))
print(Solution().maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
print(Solution().maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))

