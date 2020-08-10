from util.common_imports import *


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0

        ans = 0
        last = "0" if s[0] == "1" else "1"
        count_last, count_cur = 0, 0
        for i in range(len(s)):
            cur = s[i]
            if cur != last:
                count_cur += 1
            else:
                ans += min(count_last, count_cur)

                last, count_last = s[i - 1], count_cur
                count_cur = 1

        ans += min(count_last, count_cur) # last
        # !也可以先全部统计一遍, 再计数, 不容易忘掉last
        return ans


print(Solution().countBinarySubstrings("00110011"))
print(Solution().countBinarySubstrings("10101"))
