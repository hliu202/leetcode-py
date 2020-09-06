from util.common_imports import *


class Solution:
    def modifyString(self, s: str) -> str:
        C = list('abcdefghijklmnopqrstuvwxyz')
        ans = ''

        def check_pre(i, idx):
            return i == 0 or C[idx] != ans[i-1]
        def check_post(i, idx):
            return i == len(s) - 1 or C[idx] != s[i+1]
                
        for i in range(0, len(s)):
            if s[i] == '?':
                idx = 0
                while not (check_pre(i, idx) and check_post(i, idx)):
                    if not check_pre(i, idx):
                        idx = (idx + 1) % 26
                    if not check_post(i, idx):
                        idx = (idx + 1) % 26

                ans += C[idx]
            else:
                ans += s[i]
        return ans

# print(Solution().modifyString(s = "?zs"))
# print(Solution().modifyString(s = "ubv?w"))
# print(Solution().modifyString(s = "j?qg??b"))
# print(Solution().modifyString(s = "??yw?ipkj?"))
print(Solution().modifyString(s = "wz???a??n")) # "wzabbaban"
