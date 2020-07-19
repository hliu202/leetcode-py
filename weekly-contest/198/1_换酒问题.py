from util.common_imports import *

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return ans

        
print(Solution().numWaterBottles(numBottles = 15, numExchange = 4))