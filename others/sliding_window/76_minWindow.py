
# 滑动窗口 https://leetcode-cn.com/problems/minimum-window-substring/solution/zui-xiao-fu-gai-zi-chuan-by-leetcode-solution/
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        R = defaultdict(int)
        for st in t:
            R[st] += 1

        D = {}

        def matched():
            if len(D) != len(R):
                return False
            for k,v in R.items():
                if D[k] < v:
                    return False
            return True

        res = ""
        l = 0
        for r in range(len(s)):
            if s[r] in R:
                if s[r] not in D:
                    D[s[r]] = 1
                else:
                    D[s[r]] += 1

                if matched():
                    # move l
                    while True:
                        if s[l] not in D:
                            l += 1
                        elif D[s[l]] == R[s[l]]:
                            # record result:
                            if res == "" or  r - l + 1 < len(res):
                                res = s[l:r+1]
                            D[s[l]] -= 1
                            if D[s[l]] == 0: del D[s[l]]

                            l += 1
                            break
                        else:
                            D[s[l]] -= 1
                            l += 1

        return res

# print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(Solution().minWindow(s = "aa", t = "aa"))
