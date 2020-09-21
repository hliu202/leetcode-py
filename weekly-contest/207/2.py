
from util.common_imports import *

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        i, n = 0, len(s)
        while i < n:
            cur_len = 1
            while i + cur_len <= n and s[i:i+cur_len] in seen:
                cur_len += 1

            if i + cur_len <= n: # 不是最后一位
                seen.add(s[i:i+cur_len])
            elif s[i:i+cur_len] not in seen:
                seen.add(s[i:i+cur_len])

            i += cur_len

        return len(seen)

# print(Solution().maxUniqueSplit(s = "ababccc"))
# print(Solution().maxUniqueSplit(s = "aba"))
# print(Solution().maxUniqueSplit(s = "aa"))
print(Solution().maxUniqueSplit(s = "addbsd")) # 5: a dd b s d
