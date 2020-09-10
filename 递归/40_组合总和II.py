
from util.common_imports import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)

        def backtrack(start, cur_tar, cur_list):
            if start == n: return

            nonlocal ans
            cur_cand = candidates[start]
            if cur_cand == cur_tar:
                cur_list.append(cur_cand)
                ans.append(cur_list)
                return
            if cur_cand > cur_tar: return

            count_cur = 1
            start += 1
            while start < n and candidates[start] == cur_cand:
                start += 1
                count_cur += 1

            # number of cur_can
            for i in range(0, count_cur + 1):
                if i * cur_cand < cur_tar:
                    backtrack(start, cur_tar - i*cur_cand, cur_list + ([cur_cand]*i))
                elif i * cur_cand == cur_tar:
                    cur_list.extend([cur_cand] * i)
                    ans.append(cur_list)
                    return
                else:
                    return

        backtrack(0, target, [])
        return ans

print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5))