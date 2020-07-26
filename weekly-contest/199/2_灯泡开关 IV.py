from util.common_imports import *


class Solution:
    def minFlips(self, target: str) -> int:
        n = 0
        last = '0'
        for i in range(len(target)):
            if target[i] == last:
                continue
            else:
                last = target[i]
                n += 1
        return n


# print(Solution().minFlips(target="10111"))
# print(Solution().minFlips(target="101"))
print(Solution().minFlips(target="00000"))
print(Solution().minFlips(target="001011101"))

