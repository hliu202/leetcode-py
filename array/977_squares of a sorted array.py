from util.common_imports import *


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [x * x for x in A]
        res.sort()
        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
