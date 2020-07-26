from util.common_imports import *


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_list = list(s)
        for i in range(len(s)):
            ii = i
            next_s = s[ii]
            while ii != indices[ii]:
                tmp_ii = indices[ii]
                tmp_next_s = s_list[tmp_ii]

                s_list[tmp_ii] = next_s
                indices[ii] = ii

                next_s = tmp_next_s
                ii = tmp_ii

        return "".join(s_list)


print(Solution().restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
print(Solution().restoreString(s="abc", indices=[0, 1, 2]))
print(Solution().restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]))

