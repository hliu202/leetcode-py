
from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        cur = 0
        D = defaultdict(int)
        D[0] += 1

        for v in A:
            cur += v
            for key, v in D.items():
                if (cur - key) % K == 0:
                    res += v
            D[cur] += 1
        return res
    
print(Solution().subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))

# 超时
