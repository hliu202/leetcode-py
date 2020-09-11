from util.common_imports import *

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(start, cur_tar, cur_list):
            if start == 10: return

            n = len(cur_list)
            if n >= k: return

            if start == cur_tar:
                if k - n == 1:
                    ans.append(cur_list + [start])
                return

            if start > cur_tar: return

            dfs(start + 1, cur_tar, cur_list)
            dfs(start + 1, cur_tar - start, cur_list + [start])

        dfs(1, n, [])
        return ans

print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(3, 9))
