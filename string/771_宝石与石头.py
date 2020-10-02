from util.common_imports import *


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jj = set(list(J))
        res = 0
        for c in S:
            if c in jj:
                res += 1
        
        return res