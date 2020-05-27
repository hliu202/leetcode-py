
from collections import defaultdict
from typing import List

# 前缀和 + 同余原理
# (P[j]−P[i]) mod K==0
# => P[j] mod K == P[i] mod K
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        cur = 0
        D = defaultdict(int)
        D[0] += 1

        for v in A:
            cur += v
            m = cur % K
            res += D[m]
            D[m] += 1
        return res
    
print(Solution().subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))

# 超时
