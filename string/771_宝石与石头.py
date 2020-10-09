from util.common_imports import *


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jj = set(J) # jj = set(list(J))
        res = 0
        for c in S:
            if c in jj:
                res += 1
        
        return res

# 1.
# return sum(S.count(i) for i in J)

# 2.
# jewelsSet = set(J)
# return sum(s in jewelsSet for s in S)