
# https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/solution/c-xiang-liang-suan-yuan-xin-jian-dan-yi-dong-by-sm/
# 圆心

# 此题难点在于如何通过两个点和一个半径确定圆心
# 垂直的充要条件是两个向量的点积为 0, 即(x1-x2)*(cx-px)+(y1-y2)*(cy-py)=0

import math
from typing import List

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def dist2(p1: List[int], p2: List[int]) -> int:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        def getCircle(p1: List[int], p2: List[int]) -> List[float]:
            mid = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            angle = math.atan((p1[0] - p2[0]) / (p2[1] - p1[1])) if p2[1] - p1[1] else math.pi / 2
            d = math.sqrt(r2 - dist2(p1, mid))
            return [mid[0] + d * math.cos(angle), mid[1] + d * math.sin(angle)]
        
        n = len(points)
        ans = 1
        eps = 1e-6
        r2 = r * r
        for i in range(n):
            for j in range(i + 1):
                if dist2(points[i], points[j]) > 4 * r2:
                    continue
                center = getCircle(points[i], points[j])
                count = 0
                for k in range(n):
                    if dist2(points[k], center) < r2 + eps:
                        count += 1
                ans = max(ans, count)
        return ans

print(Solution().numPoints(points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5))
