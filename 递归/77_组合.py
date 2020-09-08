from util.common_imports import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1,n+1)]

        all_ans = []
        for i in range(k, n+1):
            ans = self.combine(i-1, k-1)
            for L in ans:
                L.append(i)
            all_ans.extend(ans)
        return all_ans

print(Solution().combine(n = 4, k = 2))


