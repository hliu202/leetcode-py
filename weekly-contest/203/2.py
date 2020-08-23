
from util.common_imports import *


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        i = n
        ans = 0
        while i < 3*n:
            ans += piles[i]
            i += 2

        return ans

print(Solution().maxCoins(piles = [2,4,1,2,7,8]))
print(Solution().maxCoins(piles = [2,4,5]))
print(Solution().maxCoins(piles = [9,8,7,6,5,1,2,3,4]))